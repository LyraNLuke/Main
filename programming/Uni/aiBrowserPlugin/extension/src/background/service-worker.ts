/**
 * Background Service Worker for Task Breakdown Assistant
 * Handles:
 * - Extension lifecycle events
 * - Periodic syncing of task data
 * - Notification triggers
 */

chrome.runtime.onInstalled.addListener((details) => {
  if (details.reason === 'install') {
    console.log('Task Breakdown Assistant installed');
    // Could open a welcome page here
  } else if (details.reason === 'update') {
    console.log('Task Breakdown Assistant updated');
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
