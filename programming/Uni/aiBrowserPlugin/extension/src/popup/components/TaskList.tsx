import React, { useState } from 'react';
import { Task } from '../../types';
import SubtaskRow from './SubtaskRow';
import '../styles/task-list.css';

interface TaskListProps {
  tasks: Task[];
  onStartSubtask: (taskId: string, subtaskId: string) => void;
  onBack: () => void;
}

const TaskList: React.FC<TaskListProps> = ({ tasks, onStartSubtask, onBack }) => {
  const [expandedTaskId, setExpandedTaskId] = useState<string | null>(
    tasks.length > 0 ? tasks[tasks.length - 1].id : null
  );

  const currentTask = tasks.find((t) => t.id === expandedTaskId);

  if (!currentTask) {
    return <div className="no-tasks">No tasks available</div>;
  }

  const completedCount = currentTask.subtasks.filter((s) => s.status === 'completed').length;
  const progress = (completedCount / currentTask.subtasks.length) * 100;

  return (
    <div className="task-list-container">
      <div className="task-header">
        <h2>{currentTask.title}</h2>
        <button className="back-btn" onClick={onBack}>← New Task</button>
      </div>

      <div className="progress-section">
        <div className="progress-info">
          <span>Progress: {completedCount}/{currentTask.subtasks.length}</span>
        </div>
        <div className="progress-bar">
          <div className="progress-fill" style={{ width: `${progress}%` }}></div>
        </div>
      </div>

      <div className="subtasks-list">
        {currentTask.subtasks.map((subtask, index) => (
          <SubtaskRow
            key={subtask.id}
            subtask={subtask}
            taskId={currentTask.id}
            index={index + 1}
            onStart={() => onStartSubtask(currentTask.id, subtask.id)}
          />
        ))}
      </div>
    </div>
  );
};

export default TaskList;
