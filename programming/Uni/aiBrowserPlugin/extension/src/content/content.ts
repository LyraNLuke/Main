/**
 * Content Script for Task Breakdown Assistant
 * Injects a floating widget button into web pages
 */

interface FloatingButtonState {
  isMinimized: boolean;
  currentTaskId: string | null;
  currentSubtaskId: string | null;
  elapsedTime: number;
}

let state: FloatingButtonState = {
  isMinimized: true,
  currentTaskId: null,
  currentSubtaskId: null,
  elapsedTime: 0,
};

function createFloatingButton() {
  // Check if button already exists
  if (document.getElementById('task-assistant-widget')) {
    return;
  }

  const container = document.createElement('div');
  container.id = 'task-assistant-widget';
  container.style.cssText = `
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 10000;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  `;

  const button = document.createElement('button');
  button.id = 'task-assistant-btn';
  button.style.cssText = `
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    cursor: pointer;
    font-size: 24px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    transition: all 0.3s;
    display: flex;
    align-items: center;
    justify-content: center;
  `;
  button.innerHTML = '✓';
  button.title = 'Task Breakdown Assistant';

  button.addEventListener('mouseover', () => {
    button.style.transform = 'scale(1.1)';
    button.style.boxShadow = '0 6px 20px rgba(102, 126, 234, 0.4)';
  });

  button.addEventListener('mouseout', () => {
    button.style.transform = 'scale(1)';
    button.style.boxShadow = '0 4px 15px rgba(0, 0, 0, 0.2)';
  });

  button.addEventListener('click', () => {
    chrome.runtime.sendMessage({ action: 'openPopup' });
  });

  // Allow dragging
  let isDragging = false;
  let offsetX = 0;
  let offsetY = 0;

  button.addEventListener('mousedown', (e) => {
    isDragging = true;
    offsetX = e.clientX - button.getBoundingClientRect().left;
    offsetY = e.clientY - button.getBoundingClientRect().top;
  });

  document.addEventListener('mousemove', (e) => {
    if (isDragging && container) {
      container.style.right = `${window.innerWidth - e.clientX + offsetX}px`;
      container.style.bottom = `${window.innerHeight - e.clientY + offsetY}px`;
    }
  });

  document.addEventListener('mouseup', () => {
    isDragging = false;
  });

  container.appendChild(button);
  document.body.appendChild(container);

  // Listen for storage changes to update minimized view
  chrome.storage.onChanged.addListener((changes, areaName) => {
    if (areaName === 'local' && changes.taskBreakdownSession) {
      updateMinimizedDisplay(changes.taskBreakdownSession.newValue);
    }
  });

  // Initial update
  chrome.storage.local.get(['taskBreakdownSession'], (result) => {
    if (result.taskBreakdownSession) {
      updateMinimizedDisplay(result.taskBreakdownSession);
    }
  });
}

function updateMinimizedDisplay(session: any) {
  const button = document.getElementById('task-assistant-btn');
  if (!button || !session) return;

  const { currentTaskId, currentSubtaskId, tasks } = session;

  if (currentSubtaskId && currentTaskId) {
    const task = tasks.find((t: any) => t.id === currentTaskId);
    if (task) {
      const subtask = task.subtasks.find((s: any) => s.id === currentSubtaskId);
      if (subtask) {
        button.title = `${subtask.title}\nTime: ${formatTime(subtask.timeSpent)}`;
      }
    }
  }
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

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', createFloatingButton);
} else {
  createFloatingButton();
}
