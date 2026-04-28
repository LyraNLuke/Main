export interface Task {
  id: string;
  title: string;
  description: string;
  subtasks: Subtask[];
  createdAt: number;
}

export interface Subtask {
  id: string;
  title: string;
  description?: string;
  status: 'pending' | 'in-progress' | 'paused' | 'completed';
  timeSpent: number; // in seconds
  startTime?: number;
  createdAt: number;
}

export interface Session {
  currentTaskId: string | null;
  currentSubtaskId: string | null;
  tasks: Task[];
  lastUpdated: number;
}
