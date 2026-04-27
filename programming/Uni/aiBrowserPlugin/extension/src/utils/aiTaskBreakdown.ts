import { Subtask } from '../types';

/**
 * Breaks down a main task into smaller subtasks using AI
 * Currently supports: Ollama (local), and can be extended to other providers
 */
export async function breakdownTask(mainTask: string): Promise<Subtask[]> {
  try {
    // Try Ollama first (local LLM - free)
    return await breakdownWithOllama(mainTask);
  } catch (error) {
    console.warn('Ollama not available, trying fallback method:', error);
    // Fallback to simple rule-based breakdown
    return fallbackBreakdown(mainTask);
  }
}

/**
 * Uses Ollama (local LLM) to break down tasks
 * Download from: https://ollama.ai
 * Default model: llama2 (or any installed model)
 */
async function breakdownWithOllama(mainTask: string): Promise<Subtask[]> {
  const ollamaUrl = 'http://localhost:11434/api/generate';
  
  const prompt = `You are a task breakdown expert. Break down the following main task into 3-7 smaller, actionable subtasks that are easier to handle. Return ONLY a JSON array with no additional text. Each item should have a "title" and optional "description".

Main task: "${mainTask}"

Return format:
[
  {"title": "Subtask 1", "description": "Description"},
  {"title": "Subtask 2", "description": "Description"}
]`;

  try {
    const response = await fetch(ollamaUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'llama2',
        prompt: prompt,
        stream: false,
      }),
    });

    if (!response.ok) {
      throw new Error(`Ollama error: ${response.statusText}`);
    }

    const data = await response.json();
    const responseText = data.response;

    // Extract JSON from response
    const jsonMatch = responseText.match(/\[[\s\S]*\]/);
    if (!jsonMatch) {
      throw new Error('Could not extract JSON from response');
    }

    const subtasksData = JSON.parse(jsonMatch[0]);
    
    return subtasksData.map((item: any, index: number) => ({
      id: `subtask-${Date.now()}-${index}`,
      title: item.title,
      description: item.description || '',
      status: 'pending' as const,
      timeSpent: 0,
      createdAt: Date.now(),
    }));
  } catch (error) {
    console.error('Ollama breakdown failed:', error);
    throw error;
  }
}

/**
 * Fallback breakdown using simple heuristics (works without AI)
 */
function fallbackBreakdown(mainTask: string): Subtask[] {
  const keywords = mainTask.toLowerCase();
  const subtasks: Subtask[] = [];

  // Simple heuristic-based breakdown
  if (keywords.includes('learn') || keywords.includes('study')) {
    subtasks.push(
      {
        id: `subtask-${Date.now()}-0`,
        title: 'Research the topic',
        description: 'Find reliable resources and materials',
        status: 'pending',
        timeSpent: 0,
        createdAt: Date.now(),
      },
      {
        id: `subtask-${Date.now()}-1`,
        title: 'Create study notes',
        description: 'Organize key concepts and information',
        status: 'pending',
        timeSpent: 0,
        createdAt: Date.now(),
      },
      {
        id: `subtask-${Date.now()}-2`,
        title: 'Practice and review',
        description: 'Test your understanding with examples',
        status: 'pending',
        timeSpent: 0,
        createdAt: Date.now(),
      }
    );
  } else if (keywords.includes('build') || keywords.includes('create')) {
    subtasks.push(
      {
        id: `subtask-${Date.now()}-0`,
        title: 'Plan the project',
        description: 'Define requirements and structure',
        status: 'pending',
        timeSpent: 0,
        createdAt: Date.now(),
      },
      {
        id: `subtask-${Date.now()}-1`,
        title: 'Set up development environment',
        description: 'Install dependencies and tools',
        status: 'pending',
        timeSpent: 0,
        createdAt: Date.now(),
      },
      {
        id: `subtask-${Date.now()}-2`,
        title: 'Implement core features',
        description: 'Write the main functionality',
        status: 'pending',
        timeSpent: 0,
        createdAt: Date.now(),
      },
      {
        id: `subtask-${Date.now()}-3`,
        title: 'Test and debug',
        description: 'Identify and fix issues',
        status: 'pending',
        timeSpent: 0,
        createdAt: Date.now(),
      }
    );
  } else {
    // Generic breakdown
    subtasks.push(
      {
        id: `subtask-${Date.now()}-0`,
        title: 'Understand the requirements',
        description: 'Clarify what needs to be done',
        status: 'pending',
        timeSpent: 0,
        createdAt: Date.now(),
      },
      {
        id: `subtask-${Date.now()}-1`,
        title: 'Make a plan',
        description: 'Organize your approach',
        status: 'pending',
        timeSpent: 0,
        createdAt: Date.now(),
      },
      {
        id: `subtask-${Date.now()}-2`,
        title: 'Execute the plan',
        description: 'Implement your strategy',
        status: 'pending',
        timeSpent: 0,
        createdAt: Date.now(),
      },
      {
        id: `subtask-${Date.now()}-3`,
        title: 'Review and refine',
        description: 'Check and improve your work',
        status: 'pending',
        timeSpent: 0,
        createdAt: Date.now(),
      }
    );
  }

  return subtasks;
}
