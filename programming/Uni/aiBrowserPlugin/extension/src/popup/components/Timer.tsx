import React, { useState, useEffect } from 'react';
import { Subtask } from '../../types';
import { updateSubtaskStatus, addTimeToSubtask, loadSession, saveSession } from '../../utils/storage';
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

  const handleStartClick = async () => {
    if (timerState === 'idle') {
      setTimerState('countdown');
      setCountdownValue(5);
      onStart();
      await updateSubtaskStatus(taskId, subtask.id, 'in-progress');
    }
  };

  const handlePauseClick = async () => {
    if (timerState === 'running') {
      setTimerState('paused');
      if (intervalId) clearInterval(intervalId);
    }
  };

  const handleResumeClick = () => {
    if (timerState === 'paused') {
      setTimerState('running');
    }
  };

  const handleStopClick = async () => {
    setTimerState('idle');
    if (intervalId) clearInterval(intervalId);
    await updateSubtaskStatus(taskId, subtask.id, 'completed');
  };

  // Countdown timer effect
  useEffect(() => {
    if (timerState === 'countdown') {
      if (countdownValue > 0) {
        const timeout = setTimeout(() => {
          setCountdownValue(countdownValue - 1);
        }, 1000);
        return () => clearTimeout(timeout);
      } else {
        // Countdown finished, start stopwatch
        setTimerState('running');
        setElapsedTime(subtask.timeSpent);
      }
    }
  }, [timerState, countdownValue, subtask.timeSpent]);

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
