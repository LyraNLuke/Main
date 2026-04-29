import { Session, Task, Subtask } from '../types';

const STORAGE_KEY = 'taskBreakdownSession';

export async function loadSession(): Promise<Session> {
  return new Promise((resolve) => {
    chrome.storage.local.get([STORAGE_KEY], (result) => {
      if (result[STORAGE_KEY]) {
        resolve(result[STORAGE_KEY]);
      } else {
        resolve({
          currentTaskId: null,
          currentSubtaskId: null,
          tasks: [],
          lastUpdated: Date.now(),
        });
      }
    });
  });
}

export async function saveSession(session: Session): Promise<void> {
  return new Promise((resolve) => {
    chrome.storage.local.set({ [STORAGE_KEY]: { ...session, lastUpdated: Date.now() } }, () => {
      resolve();
    });
  });
}

export async function addTask(task: Task): Promise<void> {
  const session = await loadSession();
  session.tasks.push(task);
  await saveSession(session);
}

export async function updateSubtaskStatus(
  taskId: string,
  subtaskId: string,
  status: 'pending' | 'in-progress' | 'paused' | 'completed'
): Promise<void> {
  const session = await loadSession();
  const task = session.tasks.find((t) => t.id === taskId);
  if (task) {
    const subtask = task.subtasks.find((s) => s.id === subtaskId);
    if (subtask) {
      if (status === 'paused' || status === 'completed') {
        if (subtask.startTime) {
          subtask.timeSpent += Math.floor((Date.now() - subtask.startTime) / 1000);
          delete subtask.startTime;
        }
      }

      subtask.status = status;

      if (status === 'in-progress') {
        subtask.startTime = Date.now();
      }

      if (status === 'pending') {
        delete subtask.startTime;
      }

      if (status !== 'in-progress' && session.currentTaskId === taskId && session.currentSubtaskId === subtaskId) {
        session.currentTaskId = null;
        session.currentSubtaskId = null;
      }

      await saveSession(session);
    }
  }
}

export async function addTimeToSubtask(
  taskId: string,
  subtaskId: string,
  seconds: number
): Promise<void> {
  const session = await loadSession();
  const task = session.tasks.find((t) => t.id === taskId);
  if (task) {
    const subtask = task.subtasks.find((s) => s.id === subtaskId);
    if (subtask) {
      subtask.timeSpent += seconds;
      if (subtask.status === 'in-progress') {
        subtask.startTime = Date.now();
      }
      await saveSession(session);
    }
  }
}

export async function setCurrentSubtask(
  taskId: string | null,
  subtaskId: string | null
): Promise<void> {
  const session = await loadSession();
  session.currentTaskId = taskId;
  session.currentSubtaskId = subtaskId;
  await saveSession(session);
}
