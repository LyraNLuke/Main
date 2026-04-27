# Project Overview: AI Task Breakdown Assistant

## What This Does

This is a **Chrome extension** that helps you break down large, overwhelming tasks into smaller, manageable subtasks using AI, and tracks how much time you spend on each one.

### The User Flow

```
1. User clicks floating button in browser corner
   ↓
2. Opens popup, enters main task
   ↓
3. AI breaks it into 3-7 smaller subtasks
   ↓
4. User sees list of subtasks with progress bar
   ↓
5. User clicks "Start" on a subtask
   ↓
6. 5-second countdown (get ready!)
   ↓
7. Stopwatch starts automatically
   ↓
8. User can pause/resume/mark done
   ↓
9. Time is saved automatically
```

## Architecture Overview

### Three Main Parts

```
┌─────────────────────────────────────────────────────────┐
│                    CHROME EXTENSION                      │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌──────────────────────────────────────────────────┐   │
│  │          POPUP (UI/React Components)             │   │
│  │  - TaskInput: Text input for task                 │   │
│  │  - TaskList: List of subtasks                     │   │
│  │  - SubtaskRow: Individual subtask display         │   │
│  │  - Timer: Countdown + Stopwatch                   │   │
│  │  - Styling: Modern gradient purple theme          │   │
│  └──────────────────────────────────────────────────┘   │
│                      ↓                                    │
│  ┌──────────────────────────────────────────────────┐   │
│  │       BACKGROUND (Service Worker)                │   │
│  │  - Lifecycle management                          │   │
│  │  - Message routing                               │   │
│  │  - Sync/notification logic                       │   │
│  └──────────────────────────────────────────────────┘   │
│                      ↓                                    │
│  ┌──────────────────────────────────────────────────┐   │
│  │        CONTENT SCRIPT (Injected)                 │   │
│  │  - Floating widget button                        │   │
│  │  - Updates when tasks change                     │   │
│  │  - Draggable/movable                             │   │
│  └──────────────────────────────────────────────────┘   │
│                      ↓                                    │
│  ┌──────────────────────────────────────────────────┐   │
│  │      UTILITIES & DATA LAYER                      │   │
│  │  - aiTaskBreakdown.ts: Talks to Ollama/AI        │   │
│  │  - storage.ts: Manages browser storage           │   │
│  │  - types/index.ts: TypeScript definitions        │   │
│  └──────────────────────────────────────────────────┘   │
│                      ↓                                    │
└─────────────────────────────────────────────────────────┘
                      ↓
           ┌──────────────────────┐
           │  CHROME STORAGE API  │
           │  (Local Storage)     │
           │  All data persists   │
           └──────────────────────┘
                      ↓
         ┌────────────────────────┐
         │  OLLAMA (Free LLM)     │
         │  localhost:11434       │
         │  Breaks down tasks     │
         └────────────────────────┘
```

## File Structure

```
extension/
│
├── src/                           # Source code
│   │
│   ├── popup/                     # React UI for the popup
│   │   ├── App.tsx                # Main React component
│   │   ├── index.tsx              # React entry point
│   │   ├── components/
│   │   │   ├── TaskInput.tsx      # ← User enters main task
│   │   │   ├── TaskList.tsx       # ← Shows subtasks & progress
│   │   │   ├── SubtaskRow.tsx     # ← Individual subtask
│   │   │   └── Timer.tsx          # ← Countdown + stopwatch ⏱️
│   │   └── styles/                # CSS styling
│   │       ├── popup.css
│   │       ├── task-input.css
│   │       ├── task-list.css
│   │       ├── subtask-row.css
│   │       └── timer.css
│   │
│   ├── background/
│   │   └── service-worker.ts      # ← Extension lifecycle & messages
│   │
│   ├── content/
│   │   └── content.ts             # ← Floating button in web pages
│   │
│   ├── utils/
│   │   ├── aiTaskBreakdown.ts     # ← Connects to Ollama/AI
│   │   └── storage.ts             # ← Handles Chrome storage
│   │
│   └── types/
│       └── index.ts               # ← TypeScript types
│
├── public/
│   ├── popup.html                 # ← HTML template for popup
│   └── styles/
│       └── content.css            # ← Floating button styles
│
├── manifest.json                  # ← Extension configuration
├── package.json                   # ← Dependencies
├── tsconfig.json                  # ← TypeScript config
├── webpack.config.js              # ← Build configuration
│
└── Documentation
    ├── README.md                  # ← Full docs
    ├── QUICKSTART.md              # ← 5-min setup
    ├── SETUP.md                   # ← Detailed setup
    └── PROJECT_OVERVIEW.md        # ← This file!
```

## Data Flow

### 1. Task Creation
```
User enters task → TaskInput component calls breakdownTask() 
→ aiTaskBreakdown.ts connects to Ollama 
→ Ollama returns subtasks 
→ Saved to Chrome storage
```

### 2. Starting a Subtask
```
User clicks "Start" 
→ Timer shows 5-second countdown 
→ Countdown ends, stopwatch starts 
→ Timer increments every second 
→ Auto-saves every 10 seconds to storage
```

### 3. Minimized View
```
User minimizes popup 
→ Content script checks storage 
→ Floating button title shows current task + time elapsed
```

## Key Technologies

### Frontend
- **React 18** - UI components
- **TypeScript** - Type safety
- **CSS3** - Modern styling with gradients & animations

### Backend/Services
- **Ollama** - Free local LLM (runs on your computer)
- **Chrome Storage API** - Local data persistence

### Build Tools
- **Webpack** - Bundler for multiple entry points
- **Babel** - JavaScript transpiler
- **TypeScript Compiler** - Type checking

## How AI Task Breakdown Works

### With Ollama (Recommended)
```
1. User enters: "Learn machine learning"
2. Extension sends to Ollama: "Break this into 3-7 subtasks"
3. Ollama (using llama2 model) returns:
   - Research ML basics and algorithms
   - Set up Python environment and libraries
   - Work through hands-on tutorials
   - Build a simple ML project
   - Review and optimize results
4. Extension displays these subtasks
```

### Fallback (If Ollama not available)
```
Extension uses rule-based breakdown:
- "Learn" tasks → Research, Take notes, Practice
- "Build" tasks → Plan, Setup, Code, Test, Review
- Generic → Understand, Plan, Execute, Review
```

## Storage Structure

```javascript
{
  currentTaskId: "task-1234567890",
  currentSubtaskId: "subtask-1234567890",
  tasks: [
    {
      id: "task-1234567890",
      title: "Learn machine learning",
      description: "",
      subtasks: [
        {
          id: "subtask-1234567890-0",
          title: "Research ML basics and algorithms",
          description: "Find reliable resources and materials",
          status: "completed",  // 'pending' | 'in-progress' | 'completed'
          timeSpent: 1800,      // seconds
          startTime: 1234567890,
          createdAt: 1234567890
        },
        // ... more subtasks
      ],
      createdAt: 1234567890
    }
  ],
  lastUpdated: 1234567890
}
```

## Installation Quick Summary

```bash
# 1. Setup
npm install
npm run build

# 2. Chrome setup
# → Go to chrome://extensions/
# → Enable Developer Mode
# → Load unpacked → select dist/ folder

# 3. Make sure Ollama is running
ollama pull llama2
ollama serve

# 4. Click the purple button on any webpage!
```

## Common Questions

### Q: Do I need internet?
A: No! Ollama runs locally on your computer. Everything is offline (except visiting websites).

### Q: Where is my data stored?
A: Locally in your browser's storage. Only on your computer.

### Q: Can I use this on other browsers?
A: Currently Chrome only. Firefox version could be added.

### Q: What if I don't want to use Ollama?
A: The extension falls back to simple rule-based breakdown. Or you can modify the AI backend.

### Q: How much does this cost?
A: Nothing! Ollama is completely free.

## Extension Lifecycle

```
1. User installs extension
   ↓
2. manifest.json is read by Chrome
   ↓
3. Service worker starts in background
   ↓
4. Content script injected into web pages
   ↓
5. Floating button appears in bottom-right
   ↓
6. User clicks button → popup opens
   ↓
7. Data saved to Chrome storage
   ↓
8. Widget updates to show current task
```

## Building and Loading

### Development
```bash
npm run dev      # Watch mode - auto-rebuilds on changes
# Reload extension in chrome://extensions/ after each change
```

### Production
```bash
npm run build    # One-time build
# Load dist/ folder in Chrome
```

### Debugging
```
1. Right-click extension icon → Options (if added)
2. Open Chrome DevTools (F12) on any webpage
3. Right-click floating button → Inspect
4. Open chrome://extensions/ → Details → Extension errors
```

---

**Ready to build?** Start with [QUICKSTART.md](./QUICKSTART.md)!
