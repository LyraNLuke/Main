import React, { useState, useEffect } from 'react';
import { Subtask } from '../../types';
import {
  updateSubtaskStatus,
  addTimeToSubtask,
  loadSession,
  saveSession,
  setCurrentSubtask,
} from '../../utils/storage';
import '../styles/timer.css';

interface TimerProps {
  subtask: Subtask;
  taskId: string;
  onStart: () => void;
}

type TimerState = 'idle' | 'countdown' | 'running' | 'paused';

const Timer: React.FC<TimerProps> = ({ subtask, taskId, onStart }) => {
  const [timerState, setTimerState] = useState<TimerState>('idle');
  const [countdownValue, setCountdownValue] = useState(5);
  const [elapsedTime, setElapsedTime] = useState(subtask.timeSpent);
  const [intervalId, setIntervalId] = useState<NodeJS.Timeout | null>(null);

  useEffect(() => {
    return () => {
      if (intervalId) clearInterval(intervalId);
    };
  }, [intervalId]);

  const handleStartClick = () => {
    if (timerState === 'idle') {
      setTimerState('countdown');
      setCountdownValue(5);
      onStart();
    }
  };

  const handlePauseClick = async () => {
    if (timerState === 'running') {
      setTimerState('paused');
      if (intervalId) {
        clearInterval(intervalId);
        setIntervalId(null);
      }
      await updateSubtaskStatus(taskId, subtask.id, 'paused');
      await setCurrentSubtask(null, null);
    }
  };

  const handleResumeClick = async () => {
    if (timerState === 'paused') {
      await setCurrentSubtask(taskId, subtask.id);
      await updateSubtaskStatus(taskId, subtask.id, 'in-progress');
      setTimerState('running');
    }
  };

  const handleStopClick = async () => {
    setTimerState('idle');
    if (intervalId) {
      clearInterval(intervalId);
      setIntervalId(null);
    }
    await updateSubtaskStatus(taskId, subtask.id, 'completed');
    await setCurrentSubtask(null, null);
  };

  // Countdown timer effect
  useEffect(() => {
    // Store countdown state in Chrome storage for content script to display
    if (timerState === 'countdown') {
      if (typeof chrome !== 'undefined' && chrome.storage) {
        chrome.storage.local.set({ 
          timerCountdown: { taskId, subtaskId: subtask.id, value: countdownValue }
        });
      }

      if (countdownValue > 0) {
        const timeout = setTimeout(() => {
          setCountdownValue(countdownValue - 1);
        }, 1000);
        return () => clearTimeout(timeout);
      } else {
        // Countdown finished, start stopwatch and record the start moment.
        const startRunning = async () => {
          await updateSubtaskStatus(taskId, subtask.id, 'in-progress');
          setTimerState('running');
          setElapsedTime(subtask.timeSpent);
          // Clear countdown from storage
          if (typeof chrome !== 'undefined' && chrome.storage) {
            chrome.storage.local.set({ timerCountdown: null });
          }
        };
        startRunning();
      }
    } else {
      // Clear countdown from storage when not in countdown mode
      if (typeof chrome !== 'undefined' && chrome.storage && timerState !== undefined) {
        chrome.storage.local.set({ timerCountdown: null });
      }
    }
  }, [timerState, countdownValue, subtask.timeSpent, taskId, subtask.id]);

  // Stopwatch effect
  useEffect(() => {
    if (timerState === 'running') {
      const id = setInterval(() => {
        setElapsedTime((prev) => {
          const newTime = prev + 1;
          // Auto-save every 10 seconds
          if (newTime % 10 === 0) {
            addTimeToSubtask(taskId, subtask.id, 10);
          }
          return newTime;
        });
      }, 1000);
      setIntervalId(id);
    }
  }, [timerState, taskId, subtask.id]);

  const formatTime = (seconds: number) => {
    const hrs = Math.floor(seconds / 3600);
    const mins = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    
    return `${String(hrs).padStart(2, '0')}:${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  };

  return (
    <div className="timer-container">
      {timerState === 'idle' && (
        <div className="timer-idle">
          <button className="start-btn" onClick={handleStartClick}>
            ▶ Start Task
          </button>
        </div>
      )}

      {timerState === 'countdown' && (
        <div className="timer-countdown">
          <div className="countdown-display">{countdownValue}</div>
          <p className="countdown-text">Get ready...</p>
        </div>
      )}

      {(timerState === 'running' || timerState === 'paused') && (
        <div className="timer-active">
          <div className="timer-display">{formatTime(elapsedTime)}</div>
          <div className="timer-controls">
            {timerState === 'running' && (
              <>
                <button className="pause-btn" onClick={handlePauseClick}>
                  ⏸ Pause
                </button>
                <button className="stop-btn" onClick={handleStopClick}>
                  ⏹ Mark Done
                </button>
              </>
            )}
            {timerState === 'paused' && (
              <>
                <button className="resume-btn" onClick={handleResumeClick}>
                  ▶ Resume
                </button>
                <button className="stop-btn" onClick={handleStopClick}>
                  ⏹ Mark Done
                </button>
              </>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default Timer;
