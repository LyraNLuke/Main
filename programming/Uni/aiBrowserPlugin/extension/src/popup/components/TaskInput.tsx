import React, { useState } from 'react';
import { Task } from '../../types';
import { breakdownTask } from '../../utils/aiTaskBreakdown';
import '../styles/task-input.css';

interface TaskInputProps {
  onSubmit: (task: Task) => void;
  isLoading: boolean;
}

const TaskInput: React.FC<TaskInputProps> = ({ onSubmit, isLoading }) => {
  const [input, setInput] = useState('');
  const [error, setError] = useState('');
  const [isBreakingDown, setIsBreakingDown] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!input.trim()) {
      setError('Please enter a task');
      return;
    }

    setError('');
    setIsBreakingDown(true);

    try {
      const subtasks = await breakdownTask(input);
      
      const task: Task = {
        id: `task-${Date.now()}`,
        title: input,
        description: '',
        subtasks,
        createdAt: Date.now(),
      };

      onSubmit(task);
      setInput('');
    } catch (err) {
      setError('Failed to break down task. Please try again.');
      console.error(err);
    } finally {
      setIsBreakingDown(false);
    }
  };

  return (
    <div className="task-input-container">
      <h1>Task Breakdown Assistant</h1>
      <p className="subtitle">Enter your task and we'll break it down into smaller steps</p>
      
      <form onSubmit={handleSubmit}>
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="What task do you want to work on?"
          disabled={isBreakingDown || isLoading}
          rows={4}
        />
        
        {error && <div className="error-message">{error}</div>}
        
        <button 
          type="submit" 
          disabled={isBreakingDown || isLoading || !input.trim()}
          className="submit-btn"
        >
          {isBreakingDown ? 'Breaking down task...' : 'Break Down Task'}
        </button>

        <div className="info-box">
          <p>💡 <strong>Tip:</strong> For best results, use Ollama with a local LLM model. 
            <a href="https://ollama.ai" target="_blank" rel="noopener noreferrer">Download Ollama</a>
          </p>
        </div>
      </form>
    </div>
  );
};

export default TaskInput;
