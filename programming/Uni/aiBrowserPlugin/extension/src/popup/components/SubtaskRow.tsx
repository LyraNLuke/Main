import React, { useState } from 'react';
import { Subtask } from '../../types';
import Timer from './Timer';
import '../styles/subtask-row.css';

interface SubtaskRowProps {
  subtask: Subtask;
  taskId: string;
  index: number;
  onStart: () => void;
}

const SubtaskRow: React.FC<SubtaskRowProps> = ({ subtask, taskId, index, onStart }) => {
  const [isExpanded, setIsExpanded] = useState(false);

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'completed':
        return '✓';
      case 'in-progress':
        return '⏱';
      default:
        return '◯';
    }
  };

  const formatTime = (seconds: number) => {
    const hrs = Math.floor(seconds / 3600);
    const mins = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    
    if (hrs > 0) {
      return `${hrs}h ${mins}m ${secs}s`;
    } else if (mins > 0) {
      return `${mins}m ${secs}s`;
    } else {
      return `${secs}s`;
    }
  };

  return (
    <div className={`subtask-row ${isExpanded ? 'expanded' : ''} ${subtask.status}`}>
      <div className="subtask-header" onClick={() => setIsExpanded(!isExpanded)}>
        <div className="subtask-info">
          <span className="status-icon">{getStatusIcon(subtask.status)}</span>
          <span className="index">{index}.</span>
          <span className="title">{subtask.title}</span>
        </div>
        
        <div className="subtask-meta">
          {subtask.timeSpent > 0 && (
            <span className="time-badge">{formatTime(subtask.timeSpent)}</span>
          )}
          <span className="expand-icon">{isExpanded ? '▼' : '▶'}</span>
        </div>
      </div>

      {isExpanded && (
        <div className="subtask-content">
          {subtask.description && (
            <p className="description">{subtask.description}</p>
          )}
          
          <Timer 
            subtask={subtask}
            taskId={taskId}
            onStart={onStart}
          />
        </div>
      )}
    </div>
  );
};

export default SubtaskRow;
