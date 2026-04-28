/**
 * Background Service Worker for Task Breakdown Assistant
 * Handles:
 * - Extension lifecycle events
 * - Periodic syncing of task data
 * - Notification triggers
 */

let popupWindowId: number | null = null;

chrome.runtime.onInstalled.addListener((details) => {
  if (details.reason === 'install') {
    console.log('Task Breakdown Assistant installed');
    // Could open a welcome page here
  } else if (details.reason === 'update') {
    console.log('Task Breakdown Assistant updated');
  }
  injectContentScriptIntoAllTabs();
});

chrome.runtime.onStartup.addListener(() => {
  injectContentScriptIntoAllTabs();
});

// Ensure the content script is injected into tabs when the service worker starts
injectContentScriptIntoAllTabs();

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete' && tab.url && /^https?:\/\//.test(tab.url)) {
    injectContentScriptIntoTab(tabId);
  }
});

chrome.tabs.onCreated.addListener((tab) => {
  if (tab.id !== undefined && tab.url && /^https?:\/\//.test(tab.url)) {
    injectContentScriptIntoTab(tab.id);
  }
});

chrome.action.onClicked.addListener((tab) => {
  const tabId = tab.id;
  if (tabId !== undefined) {
    chrome.tabs.sendMessage(tabId, { action: 'toggleWidget' }, (response) => {
      if (chrome.runtime.lastError) {
        injectContentScriptIntoTab(tabId, () => {
          chrome.tabs.sendMessage(tabId, { action: 'toggleWidget' }, () => {
            if (chrome.runtime.lastError) {
              openPopupWindowFallback();
            }
          });
        });
      }
    });
    return;
  }

  openPopupWindowFallback();
});

function injectContentScriptIntoAllTabs() {
  chrome.tabs.query({ url: ['http://*/*', 'https://*/*'] }, (tabs) => {
    for (const tab of tabs) {
      if (tab.id !== undefined) {
        injectContentScriptIntoTab(tab.id);
      }
    }
  });
}

function injectContentScriptIntoTab(tabId: number, callback?: () => void) {
  chrome.scripting.executeScript({
    target: { tabId },
    files: ['content.js'],
  }, () => {
    chrome.scripting.insertCSS({
      target: { tabId },
      files: ['styles/content.css'],
    }, () => {
      if (callback) callback();
    });
  });
}

function openPopupWindowFallback() {
  if (popupWindowId !== null) {
    const windowId = popupWindowId;
    chrome.windows.get(windowId, { populate: false }, (window) => {
      if (chrome.runtime.lastError || !window) {
        popupWindowId = null;
        createPopupWindow();
        return;
      }
      chrome.windows.update(windowId, { focused: true });
    });
    return;
  }

  createPopupWindow();
}

function createPopupWindow() {
  chrome.windows.create({
    url: chrome.runtime.getURL('popup.html'),
    type: 'popup',
    width: 520,
    height: 760,
    focused: true,
  }, (window) => {
    if (window && window.id !== undefined) {
      popupWindowId = window.id;
    }
  });
}

chrome.windows.onRemoved.addListener((windowId) => {
  if (windowId === popupWindowId) {
    popupWindowId = null;
  }
});

chrome.alarms.create('syncData', { periodInMinutes: 5 });

chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === 'syncData') {
    console.log('Syncing task data...');
    // Could add cloud sync logic here
  }
});

// Listen for messages from content script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'getTaskStatus') {
    chrome.storage.local.get(['taskBreakdownSession'], (result) => {
      sendResponse(result.taskBreakdownSession || null);
    });
    return true; // Will respond asynchronously
  }
});
