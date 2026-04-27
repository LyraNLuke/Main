# AI Task Breakdown Assistant - Browser Extension

A Chrome extension that breaks down large tasks into smaller, manageable subtasks using AI, and helps you track time spent on each subtask.

## Features

- ✨ **AI-Powered Task Breakdown**: Uses Ollama (free, local LLM) to intelligently break down tasks
- ⏱️ **Built-in Timer**: 5-second countdown before starting each subtask
- ⏱️ **Stopwatch**: Track time spent on each task
- 💾 **Local Storage**: All data stored locally in your browser
- 🎯 **Progress Tracking**: Visual progress bar showing completion status
- 📌 **Floating Widget**: Draggable button in the corner of your browser
- 🎨 **Modern UI**: Clean, gradient-based interface

## Installation

### Prerequisites

1. **Node.js** (v16+) and npm installed
2. **Chrome** (or Chromium-based browser like Edge, Brave)
3. **Ollama** (for AI task breakdown)

### Setup Instructions

#### Step 1: Install Ollama (Free Local LLM)

1. Download from: https://ollama.ai
2. Install and run Ollama
3. Pull a model (in terminal):
   ```bash
   ollama pull llama2
   ```
   Ollama will start running on `http://localhost:11434` by default

#### Step 2: Build the Extension

1. Navigate to the extension directory:
   ```bash
   cd extension
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Build the extension:
   ```bash
   npm run build
   ```

   This creates a `dist/` folder with compiled files.

#### Step 3: Load Extension in Chrome

1. Open Chrome and go to: `chrome://extensions/`
2. Enable **Developer Mode** (top right toggle)
3. Click **Load unpacked**
4. Select the `extension/dist/` folder
5. The extension is now installed! 🎉

## Usage

1. Click the floating button (purple circle with checkmark) in the bottom-right corner of any webpage
2. Enter your main task in the text area
3. Click **Break Down Task**
4. Wait for AI to generate subtasks
5. Click on a subtask to expand it
6. Click **Start Task** to begin the timer:
   - 5-second countdown
   - Automatic stopwatch start
   - Time is automatically saved
7. Click **Pause** to pause, **Resume** to continue, or **Mark Done** to complete
8. When minimized, the floating button shows the current subtask and elapsed time

## How to Use with Ollama

### First Time Setup

1. **Download Ollama**: Visit https://ollama.ai and download the installer
2. **Install**: Run the installer and follow prompts
3. **Pull a Model**:
   ```bash
   # In terminal/command prompt
   ollama pull llama2
   ```
4. **Ollama runs automatically** on `http://localhost:11434`

### During Use

- **Keep Ollama running** in the background while using the extension
- The extension will automatically use Ollama to break down tasks
- If Ollama is not running, the extension falls back to simple rule-based breakdown

### Troubleshooting Ollama

- **"Failed to break down task" error?** Make sure:
  - Ollama is running (it usually runs as a background service)
  - You've pulled at least one model: `ollama pull llama2`
  - Ollama is listening on `http://localhost:11434`

- **To check if Ollama is running**:
  ```bash
  curl http://localhost:11434
  ```
  If you get a response, Ollama is running!

## Development

### Project Structure

```
extension/
├── src/
│   ├── popup/           # React UI components
│   │   ├── components/  # React components
│   │   ├── styles/      # CSS styling
│   │   └── index.tsx    # React entry point
│   ├── background/      # Service worker
│   ├── content/         # Content script (floating widget)
│   ├── utils/           # Utilities (AI, storage)
│   └── types/           # TypeScript type definitions
├── public/
│   ├── popup.html       # Popup HTML
│   └── styles/          # Global styles
├── manifest.json        # Extension manifest
├── package.json         # Dependencies
├── tsconfig.json        # TypeScript config
└── webpack.config.js    # Webpack config
```

### Commands

```bash
# Development (watch mode)
npm run dev

# Production build
npm run build

# Run tests
npm run test
```

### Modifying AI Backend

To use a different AI provider instead of Ollama, edit [src/utils/aiTaskBreakdown.ts](src/utils/aiTaskBreakdown.ts):

**OpenAI Example**:
```typescript
// Replace breakdownWithOllama with:
async function breakdownWithOpenAI(mainTask: string): Promise<Subtask[]> {
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${YOUR_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'gpt-3.5-turbo',
      messages: [{
        role: 'user',
        content: `Break down this task: ${mainTask}`,
      }],
    }),
  });
  // ... parse response and return subtasks
}
```

## Storage & Privacy

- All task data is stored **locally** in your browser using Chrome's `storage.local` API
- **No data is sent to external servers** (except when using AI backends)
- With Ollama, everything runs locally on your machine

## Known Limitations

- Ollama requires setup (but it's free!)
- Local storage limit is ~10MB per extension
- Floating button only visible on regular web pages (not on Chrome extension pages)

## Future Features

- Cloud sync for task history
- Multiple AI provider support
- Task templates
- Recurring tasks
- Team collaboration

## License

MIT

## Support

Having issues? Check the troubleshooting sections above or open an issue in the repository.
