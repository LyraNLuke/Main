/**
 * Content Script for Task Breakdown Assistant
 * Injects a floating widget and panel into web pages
 */

interface WidgetState {
  isOpen: boolean;
  left: number;
  top: number;
  expandedLeft?: number;
  expandedTop?: number;
  minimizedLeft?: number;
  minimizedTop?: number;
}

const STORAGE_KEY = 'taskAssistantWidgetState';
const DEFAULT_WIDGET_WIDTH = 520;
const DEFAULT_WIDGET_HEIGHT = 760;
const MINIMIZED_WIDTH = 320;
const MINIMIZED_HEIGHT = 72;
const ROUND_BUTTON_WIDTH = 60;
const ROUND_BUTTON_HEIGHT = 60;

let widgetState: WidgetState = {
  isOpen: false,
  left: window.innerWidth - 90,
  top: window.innerHeight - 90,
};

let isDragging = false;
let pendingButtonDrag = false;
let activePointerId: number | null = null;
let dragOffsetX = 0;
let dragOffsetY = 0;
let widgetContainer: HTMLDivElement | null = null;
let panelWrapper: HTMLDivElement | null = null;
let minimizedBar: HTMLDivElement | null = null;
let minimizedTitle: HTMLDivElement | null = null;
let minimizedTime: HTMLDivElement | null = null;
let minimizedStatusIcon: HTMLSpanElement | null = null;
let toggleButton: HTMLButtonElement | null = null;
let activeSession: any = null;
let minimizedTimerInterval: number | null = null;
let countdownState: any = null;

function saveWidgetState() {
  chrome.storage.local.set({ [STORAGE_KEY]: widgetState });
}

function clampPosition(left: number, top: number, forceWidth?: number, forceHeight?: number) {
  const width = forceWidth !== undefined ? forceWidth : (widgetState.isOpen ? DEFAULT_WIDGET_WIDTH : MINIMIZED_WIDTH);
  const height = forceHeight !== undefined ? forceHeight : (widgetState.isOpen ? DEFAULT_WIDGET_HEIGHT : MINIMIZED_HEIGHT);
  const maxLeft = Math.max(10, window.innerWidth - width - 10);
  const maxTop = Math.max(10, window.innerHeight - height - 10);
  return {
    left: Math.min(Math.max(10, left), maxLeft),
    top: Math.min(Math.max(10, top), maxTop),
  };
}

function getVisibleWidgetSize() {
  if (widgetState.isOpen) {
    return { width: DEFAULT_WIDGET_WIDTH, height: DEFAULT_WIDGET_HEIGHT };
  }

  const isRoundButton = toggleButton?.style.display !== 'none';
  if (isRoundButton) {
    return { width: ROUND_BUTTON_WIDTH, height: ROUND_BUTTON_HEIGHT };
  }

  return { width: MINIMIZED_WIDTH, height: MINIMIZED_HEIGHT };
}

function applyWidgetPosition() {
  if (!widgetContainer) return;
  widgetContainer.style.left = `${widgetState.left}px`;
  widgetContainer.style.top = `${widgetState.top}px`;
}

function findActiveSubtask(session: any) {
  if (!session || !Array.isArray(session.tasks) || session.tasks.length === 0) return null;

  if (!session.currentTaskId || !session.currentSubtaskId) return null;

  const task = session.tasks.find((t: any) => t.id === session.currentTaskId);
  const subtask = task?.subtasks?.find((s: any) => s.id === session.currentSubtaskId);
  if (task && subtask) {
    if (subtask.status === 'in-progress' && subtask.startTime) {
      return { task, subtask };
    }

    if (subtask.status === 'starting' && subtask.countdownEndTime) {
      return { task, subtask };
    }

    if (
      countdownState &&
      countdownState.taskId === session.currentTaskId &&
      countdownState.subtaskId === session.currentSubtaskId
    ) {
      return { task, subtask };
    }
  }

  return null;
}

function hasActiveTask(session: any) {
  return !!findActiveSubtask(session);
}

function getActiveTaskDisplay(session: any) {
  const active = findActiveSubtask(session);
  if (!active) return null;

  const { task, subtask } = active;

  if (subtask.status === 'starting') {
    const now = Date.now();
    const remaining = subtask.countdownEndTime ? Math.max(0, Math.ceil((subtask.countdownEndTime - now) / 1000)) : 5;
    return {
      title: subtask.title,
      time: `${remaining}s`,
    };
  }

  if (
    countdownState &&
    countdownState.taskId === session.currentTaskId &&
    countdownState.subtaskId === session.currentSubtaskId
  ) {
    return {
      title: subtask.title,
      time: `${countdownState.value}s`,
    };
  }

  let seconds = subtask.timeSpent || 0;
  if (subtask.status === 'in-progress' && subtask.startTime) {
    seconds += Math.floor((Date.now() - subtask.startTime) / 1000);
  }

  return {
    title: subtask.title,
    time: formatTime(seconds),
  };
}

function refreshWidgetView() {
  if (!panelWrapper || !minimizedBar || !toggleButton || !widgetContainer) return;

  const active = hasActiveTask(activeSession);
  if (widgetState.isOpen) {
    panelWrapper.style.display = 'block';
    minimizedBar.style.display = 'none';
    toggleButton.style.display = 'none';
    widgetContainer.style.width = `${DEFAULT_WIDGET_WIDTH}px`;
    return;
  }

  if (active) {
    panelWrapper.style.display = 'none';
    minimizedBar.style.display = 'flex';
    toggleButton.style.display = 'none';
    widgetContainer.style.width = `${MINIMIZED_WIDTH}px`;
  } else {
    panelWrapper.style.display = 'none';
    minimizedBar.style.display = 'none';
    toggleButton.style.display = 'flex';
    widgetContainer.style.width = `${ROUND_BUTTON_WIDTH}px`;
    stopMinimizedTimer();
  }
}

function saveCurrentWidgetPosition() {
  if (widgetState.isOpen) {
    widgetState.expandedLeft = widgetState.left;
    widgetState.expandedTop = widgetState.top;
  } else {
    widgetState.minimizedLeft = widgetState.left;
    widgetState.minimizedTop = widgetState.top;
  }
}

function togglePanel(shouldOpen?: boolean) {
  const nextOpen = shouldOpen !== undefined ? shouldOpen : !widgetState.isOpen;
  widgetState.isOpen = nextOpen;
  if (!panelWrapper || !minimizedBar || !widgetContainer || !toggleButton) return;

  if (!hasActiveTask(activeSession) && widgetState.isOpen === false) {
    widgetState.isOpen = false;
  }

  if (widgetState.isOpen) {
    if (widgetState.minimizedLeft === undefined || widgetState.minimizedTop === undefined) {
      widgetState.minimizedLeft = widgetState.left;
      widgetState.minimizedTop = widgetState.top;
    }
    if (widgetState.expandedLeft !== undefined && widgetState.expandedTop !== undefined) {
      widgetState.left = widgetState.expandedLeft;
      widgetState.top = widgetState.expandedTop;
    }
    const clamped = clampPosition(widgetState.left, widgetState.top, DEFAULT_WIDGET_WIDTH, DEFAULT_WIDGET_HEIGHT);
    widgetState.left = clamped.left;
    widgetState.top = clamped.top;
    widgetState.expandedLeft = widgetState.left;
    widgetState.expandedTop = widgetState.top;
  } else {
    if (widgetState.expandedLeft === undefined || widgetState.expandedTop === undefined) {
      widgetState.expandedLeft = widgetState.left;
      widgetState.expandedTop = widgetState.top;
    }
    if (widgetState.minimizedLeft !== undefined && widgetState.minimizedTop !== undefined) {
      widgetState.left = widgetState.minimizedLeft;
      widgetState.top = widgetState.minimizedTop;
    }
    const isRoundButton = !hasActiveTask(activeSession);
    const width = isRoundButton ? ROUND_BUTTON_WIDTH : MINIMIZED_WIDTH;
    const height = isRoundButton ? ROUND_BUTTON_HEIGHT : MINIMIZED_HEIGHT;
    const clamped = clampPosition(widgetState.left, widgetState.top, width, height);
    widgetState.left = clamped.left;
    widgetState.top = clamped.top;
    widgetState.minimizedLeft = widgetState.left;
    widgetState.minimizedTop = widgetState.top;
  }

  applyWidgetPosition();
  saveCurrentWidgetPosition();
  saveWidgetState();
  refreshWidgetView();
}

function setMinimizedStatusIcon(active: boolean) {
  if (!minimizedStatusIcon) return;
  if (active) {
    minimizedStatusIcon.textContent = '⏳';
    minimizedStatusIcon.style.background = 'rgba(255, 243, 224, 0.9)';
    minimizedStatusIcon.style.color = '#ff9800';
  } else {
    minimizedStatusIcon.textContent = '•';
    minimizedStatusIcon.style.background = 'rgba(237, 242, 247, 0.9)';
    minimizedStatusIcon.style.color = '#65748b';
  }
}

function stopMinimizedTimer() {
  if (minimizedTimerInterval !== null) {
    window.clearInterval(minimizedTimerInterval);
    minimizedTimerInterval = null;
  }
}

function startMinimizedTimer() {
  stopMinimizedTimer();
  
  // Update immediately first
  if (activeSession && hasActiveTask(activeSession)) {
    const activeTaskDisplay = getActiveTaskDisplay(activeSession);
    if (activeTaskDisplay && minimizedTime) {
      minimizedTime.textContent = activeTaskDisplay.time;
    }
  }
  
  // Then update every 1 second
  minimizedTimerInterval = window.setInterval(() => {
    if (!activeSession || !hasActiveTask(activeSession)) {
      stopMinimizedTimer();
      return;
    }

    const activeTaskDisplay = getActiveTaskDisplay(activeSession);
    if (!activeTaskDisplay) {
      stopMinimizedTimer();
      return;
    }

    if (minimizedTime) {
      minimizedTime.textContent = activeTaskDisplay.time;
    }
  }, 1000);
}

function updateMinimizedInfo(session: any) {
  activeSession = session;
  if (!minimizedTitle || !minimizedTime) return;

  const activeTaskDisplay = getActiveTaskDisplay(session);
  if (!activeTaskDisplay) {
    minimizedTitle.textContent = 'No active task';
    minimizedTime.textContent = '00:00';
    setMinimizedStatusIcon(false);
    stopMinimizedTimer();
    widgetState.isOpen = false;
    refreshWidgetView();
    return;
  }

  minimizedTitle.textContent = activeTaskDisplay.title;
  minimizedTime.textContent = activeTaskDisplay.time;
  setMinimizedStatusIcon(true);
  startMinimizedTimer();
  refreshWidgetView();
}


function createFloatingWidget() {
  if (document.getElementById('task-assistant-widget')) {
    return;
  }

  widgetContainer = document.createElement('div');
  widgetContainer.id = 'task-assistant-widget';
  widgetContainer.style.cssText = `
    position: fixed;
    left: ${widgetState.left}px;
    top: ${widgetState.top}px;
    z-index: 2147483647;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 12px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    pointer-events: auto;
    width: ${widgetState.isOpen ? DEFAULT_WIDGET_WIDTH : MINIMIZED_WIDTH}px;
  `;

  panelWrapper = document.createElement('div');
  panelWrapper.id = 'task-assistant-panel-wrapper';
  panelWrapper.style.cssText = `
    width: 100%;
    height: ${DEFAULT_WIDGET_HEIGHT}px;
    border-radius: 24px;
    overflow: hidden;
    background: white;
    box-shadow: 0 25px 70px rgba(0, 0, 0, 0.25);
    display: ${widgetState.isOpen ? 'block' : 'none'};
  `;

  const panelHeader = document.createElement('div');
  panelHeader.style.cssText = `
    display: flex;
    align-items: center;
    justify-content: flex-end;
    background: #f8f9fb;
    padding: 8px;
    border-bottom: 1px solid rgba(0,0,0,0.08);
    cursor: grab;
  `;

  const closeButton = document.createElement('button');
  closeButton.textContent = '✕';
  closeButton.title = 'Minimize assistant panel';
  closeButton.style.cssText = `
    all: unset;
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    cursor: pointer;
    color: #222;
    background: rgba(0, 0, 0, 0.08);
    border: 1px solid rgba(0,0,0,0.1);
    transition: background 0.2s, transform 0.2s;
  `;
  closeButton.addEventListener('mouseover', () => {
    closeButton.style.background = 'rgba(0,0,0,0.14)';
    closeButton.style.transform = 'scale(1.05)';
  });
  closeButton.addEventListener('mouseout', () => {
    closeButton.style.background = 'rgba(0, 0, 0, 0.08)';
    closeButton.style.transform = 'scale(1)';
  });
  closeButton.addEventListener('click', (e) => {
    e.stopPropagation();
    togglePanel(false);
  });

  panelHeader.appendChild(closeButton);

  const iframe = document.createElement('iframe');
  iframe.src = chrome.runtime.getURL('popup.html');
  iframe.style.cssText = `
    width: 100%;
    height: calc(100% - 48px);
    border: none;
  `;

  panelWrapper.appendChild(panelHeader);
  panelWrapper.appendChild(iframe);

  minimizedBar = document.createElement('div');
  minimizedBar.id = 'task-assistant-minimized-bar';
  minimizedBar.style.cssText = `
    width: 100%;
    min-height: ${MINIMIZED_HEIGHT}px;
    border-radius: 18px;
    background: #fff;
    border: 1px solid rgba(224, 224, 224, 0.95);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.14);
    display: ${widgetState.isOpen ? 'none' : 'flex'};
    align-items: center;
    justify-content: space-between;
    padding: 12px 14px;
    gap: 12px;
    cursor: grab;
  `;

  const minimizedText = document.createElement('div');
  minimizedText.style.cssText = `
    display: flex;
    flex-direction: column;
    gap: 4px;
    min-width: 0;
  `;

  const minimizedHeader = document.createElement('div');
  minimizedHeader.style.cssText = `
    display: flex;
    align-items: center;
    gap: 10px;
    min-width: 0;
  `;

  const statusIcon = document.createElement('span');
  minimizedStatusIcon = statusIcon;
  statusIcon.id = 'task-assistant-minimized-status-icon';
  statusIcon.textContent = '⏳';
  statusIcon.style.cssText = `
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    border-radius: 12px;
    background: rgba(255, 243, 224, 0.9);
    color: #ff9800;
    font-size: 14px;
  `;

  minimizedTitle = document.createElement('div');
  minimizedTitle.id = 'task-assistant-minimized-title';
  minimizedTitle.style.cssText = `
    font-size: 15px;
    font-weight: 600;
    color: #111;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 220px;
  `;
  minimizedTitle.textContent = 'No active task';

  minimizedHeader.appendChild(statusIcon);
  minimizedHeader.appendChild(minimizedTitle);

  const minimizedMeta = document.createElement('div');
  minimizedMeta.style.cssText = `
    display: flex;
    align-items: center;
    gap: 8px;
  `;

  minimizedTime = document.createElement('div');
  minimizedTime.id = 'task-assistant-minimized-time';
  minimizedTime.style.cssText = `
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background-color: #e3f2fd;
    color: #1565c0;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 600;
    white-space: nowrap;
  `;
  minimizedTime.textContent = '00:00';

  minimizedMeta.appendChild(minimizedTime);
  minimizedText.appendChild(minimizedHeader);
  minimizedText.appendChild(minimizedMeta);

  const expandButton = document.createElement('button');
  expandButton.textContent = '▴';
  expandButton.title = 'Restore assistant panel';
  expandButton.style.cssText = `
    all: unset;
    width: 42px;
    height: 42px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
  `;
  expandButton.addEventListener('mouseover', () => {
    expandButton.style.transform = 'scale(1.05)';
    expandButton.style.boxShadow = '0 8px 18px rgba(0, 0, 0, 0.18)';
  });
  expandButton.addEventListener('mouseout', () => {
    expandButton.style.transform = 'scale(1)';
    expandButton.style.boxShadow = 'none';
  });
  expandButton.addEventListener('click', () => togglePanel(true));

  minimizedBar.appendChild(minimizedText);
  minimizedBar.appendChild(expandButton);

  toggleButton = document.createElement('button');
  toggleButton.id = 'task-assistant-toggle-btn';
  toggleButton.textContent = '✓';
  toggleButton.title = 'Open task assistant';
  toggleButton.style.cssText = `
    all: unset;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    cursor: pointer;
    user-select: none;
    transition: transform 0.2s, box-shadow 0.2s;
  `;
  toggleButton.addEventListener('mouseover', () => {
    toggleButton!.style.transform = 'scale(1.05)';
    toggleButton!.style.boxShadow = '0 6px 20px rgba(102, 126, 234, 0.4)';
  });
  toggleButton.addEventListener('mouseout', () => {
    toggleButton!.style.transform = 'scale(1)';
    toggleButton!.style.boxShadow = '0 4px 15px rgba(0, 0, 0, 0.2)';
  });

  let buttonDragStarted = false;
  toggleButton.addEventListener('click', (event) => {
    if (buttonDragStarted) {
      event.preventDefault();
      event.stopPropagation();
      buttonDragStarted = false;
      return;
    }
    togglePanel(true);
  });

  // Drag handling - only from draggable areas, not from buttons
  let dragStartX = 0;
  let dragStartY = 0;
  let pointerDownTime = 0;

  const dragStart = (event: PointerEvent) => {
    // Reject if clicking a button that's not meant for dragging
    if ((event.target as HTMLElement).closest('button')) {
      return;
    }
    
    isDragging = true;
    dragStartX = event.clientX;
    dragStartY = event.clientY;
    pointerDownTime = Date.now();
    dragOffsetX = event.clientX - widgetState.left;
    dragOffsetY = event.clientY - widgetState.top;
    event.preventDefault();

    if (widgetContainer && 'setPointerCapture' in widgetContainer) {
      widgetContainer.setPointerCapture(event.pointerId);
    }
  };

  // Only add drag listeners to the header and minimized bar areas
  panelHeader.addEventListener('pointerdown', dragStart);
  minimizedBar.addEventListener('pointerdown', dragStart);

  // Also allow dragging the round button itself
  toggleButton.addEventListener('pointerdown', (event: PointerEvent) => {
    if ((event.target as HTMLElement) === toggleButton) {
      pendingButtonDrag = true;
      activePointerId = event.pointerId;
      dragStartX = event.clientX;
      dragStartY = event.clientY;
      pointerDownTime = Date.now();
      dragOffsetX = event.clientX - widgetState.left;
      dragOffsetY = event.clientY - widgetState.top;
    }
  });

  const handlePointerMove = (event: PointerEvent) => {
    if (!widgetContainer) return;

    if (!isDragging && pendingButtonDrag && event.pointerId === activePointerId) {
      const distX = event.clientX - dragStartX;
      const distY = event.clientY - dragStartY;
      const distance = Math.sqrt(distX * distX + distY * distY);
      if (distance >= 5) {
        isDragging = true;
        pendingButtonDrag = false;
        buttonDragStarted = true;
        if ('setPointerCapture' in widgetContainer) {
          widgetContainer.setPointerCapture(event.pointerId);
        }
      }
    }

    if (!isDragging) return;

    const left = event.clientX - dragOffsetX;
    const top = event.clientY - dragOffsetY;
    const { width, height } = getVisibleWidgetSize();
    const clamped = clampPosition(left, top, width, height);

    if (clamped.left !== left || clamped.top !== top) {
      dragOffsetX = event.clientX - clamped.left;
      dragOffsetY = event.clientY - clamped.top;
    }
    
    widgetState.left = clamped.left;
    widgetState.top = clamped.top;
    applyWidgetPosition();
  };

  const handlePointerUp = (event: PointerEvent) => {
    if (!isDragging && !pendingButtonDrag) return;

    if (widgetContainer && 'releasePointerCapture' in widgetContainer) {
      widgetContainer.releasePointerCapture(event.pointerId);
    }

    const distX = event.clientX - dragStartX;
    const distY = event.clientY - dragStartY;
    const distance = Math.sqrt(distX * distX + distY * distY);

    if (isDragging && distance > 5) {
      saveCurrentWidgetPosition();
      saveWidgetState();
    }

    isDragging = false;
    pendingButtonDrag = false;
    activePointerId = null;
  };

  document.addEventListener('pointermove', handlePointerMove);
  document.addEventListener('pointerup', handlePointerUp);
  document.addEventListener('pointercancel', handlePointerUp);

  widgetContainer.appendChild(panelWrapper);
  widgetContainer.appendChild(minimizedBar);
  widgetContainer.appendChild(toggleButton);
  document.body.appendChild(widgetContainer);

  chrome.storage.onChanged.addListener((changes, areaName) => {
    if (areaName !== 'local') return;
    const savedState = changes[STORAGE_KEY]?.newValue;
    if (savedState) {
      widgetState = { ...widgetState, ...savedState };
      applyWidgetPosition();
    }
    if (changes.taskBreakdownSession) {
      updateMinimizedInfo(changes.taskBreakdownSession.newValue);
    }
    if (changes.timerCountdown) {
      countdownState = changes.timerCountdown.newValue;
      updateMinimizedInfo(activeSession);
    }
  });

  chrome.storage.local.get(['taskBreakdownSession', 'timerCountdown'], (result) => {
    countdownState = result.timerCountdown || null;
    updateMinimizedInfo(result.taskBreakdownSession || null);
  });
}

function formatTime(seconds: number): string {
  const hrs = Math.floor(seconds / 3600);
  const mins = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;

  if (hrs > 0) {
    return `${hrs}h ${mins}m`;
  } else if (mins > 0) {
    return `${mins}m ${secs}s`;
  } else {
    return `${secs}s`;
  }
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'toggleWidget') {
    togglePanel(true);
    sendResponse({ success: true });
    return;
  }

  if (request.action === 'refreshActiveTask') {
    chrome.storage.local.get(['taskBreakdownSession'], (result) => {
      updateMinimizedInfo(result.taskBreakdownSession || null);
      sendResponse({ success: true });
    });
    return true;
  }
});

function initializeWidget() {
  chrome.storage.local.get([STORAGE_KEY], (result) => {
    if (result[STORAGE_KEY]) {
      widgetState = { ...widgetState, ...result[STORAGE_KEY] };
    }
    const clamped = clampPosition(widgetState.left, widgetState.top);
    widgetState.left = clamped.left;
    widgetState.top = clamped.top;
    createFloatingWidget();
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeWidget);
} else {
  initializeWidget();
}
