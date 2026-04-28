import React, { useState, useEffect } from 'react';
import { Session, Task, Subtask } from '../types';
import { loadSession, saveSession, setCurrentSubtask } from '../utils/storage';
import TaskInput from './components/TaskInput';
import TaskList from './components/TaskList';
import './styles/popup.css';

const App: React.FC = () => {
  const [session, setSession] = useState<Session | null>(null);
  const [view, setView] = useState<'input' | 'list'>('input');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadSessionData();
  }, []);

  const loadSessionData = async () => {
    const loadedSession = await loadSession();
    setSession(loadedSession);
    if (loadedSession.tasks.length > 0) {
      setView('list');
    }
  };

  const handleTaskSubmit = async (task: Task) => {
    if (!session) return;
    
    setLoading(true);
    const updatedSession = { ...session };
    updatedSession.tasks.push(task);
    await saveSession(updatedSession);
    setSession(updatedSession);
    setView('list');
    setLoading(false);
  };

  const handleStartSubtask = async (taskId: string, subtaskId: string) => {
    await setCurrentSubtask(taskId, subtaskId);
    if (typeof chrome !== 'undefined' && chrome.runtime && chrome.runtime.sendMessage) {
      chrome.runtime.sendMessage({ action: 'refreshActiveTask' });
    }
    await loadSessionData();
  };

  if (!session) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="app">
      {view === 'input' ? (
        <TaskInput onSubmit={handleTaskSubmit} isLoading={loading} />
      ) : (
        <TaskList 
          tasks={session.tasks}
          onStartSubtask={handleStartSubtask}
          onBack={() => setView('input')}
        />
      )}
    </div>
  );
};

export default App;
