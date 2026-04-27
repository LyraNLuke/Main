# Task Decomposer

A productivity tool that uses AI to break down complex tasks into manageable components and provides a focus timer to help you tackle each part individually.

Available as both a VS Code extension and a browser extension with floating widget.

## Features

- 🤖 **AI-Powered Task Decomposition**: Break down any task into key components using AI
- ⏱️ **3-Second Focus Timer**: Get into the zone with a countdown timer before starting each component
- 📋 **Component List**: View all task components and start each one individually
- 🎯 **Floating Widget**: Browser extension with a persistent floating button in the corner of your screen

## Installation

### Browser Extension

1. Download or clone this repository
2. Open Chrome/Edge and go to `chrome://extensions/`
3. Enable "Developer mode" (top right)
4. Click "Load unpacked" and select the project folder
5. The extension will be installed and the floating widget will appear on all web pages

**Note**: You'll need to add icon files (`media/icon16.png`, `media/icon48.png`, `media/icon128.png`) for the extension to display properly. You can create simple icons or download free ones online.

### VS Code Extension

#### Prerequisites

- VS Code 1.75.0 or later
- Node.js 14+ (for development)
- npm

#### From Source

1. Clone or extract this repository
2. Install dependencies:
   ```bash
   npm install
   ```
3. Build the extension:
   ```bash
   npm run esbuild
   ```
4. Open the project in VS Code and press `F5` to run the extension in debug mode

## Usage

### Browser Extension

1. The floating **+** button appears in the bottom right corner of every web page
2. Click the button to open the Task Decomposer widget
3. Click **"Start New Task"** button
4. Enter the task you want to break down
5. The AI will analyze your task and display key components
6. Click **"Start"** on any component to begin a 3-second focus countdown
7. After the timer, you're ready to work on that component
8. Close the widget by clicking the × or clicking outside

### VS Code Extension

1. Click the **Task Decomposer** icon in the activity bar (left sidebar)
2. Click **"Start New Task"** button
3. Enter the task you want to break down
4. The AI will analyze your task and display key components
5. Click **"Start"** on any component to begin a 3-second focus countdown
6. After the timer, you're ready to work on that component

## Setup AI Integration

The tool includes a placeholder for AI integration. To enable actual AI-powered task decomposition:

### Option 1: OpenAI (GPT-3.5/GPT-4)

1. Install OpenAI package:
   ```bash
   npm install openai
   ```

2. Get an API key from [OpenAI](https://platform.openai.com/api-keys)

3. Update the `decomposeWithAI` method in [extension.ts](src/extension.ts):

   ```typescript
   private async decomposeWithAI(task: string): Promise<string[]> {
       const { Configuration, OpenAIApi } = require("openai");
       
       const configuration = new Configuration({
           apiKey: process.env.OPENAI_API_KEY,
       });
       
       const openai = new OpenAIApi(configuration);
       
       const response = await openai.createChatCompletion({
           model: "gpt-3.5-turbo",
           messages: [
               {
                   role: "system",
                   content: "You are a task decomposition expert. Break down tasks into 3-5 specific, actionable steps."
               },
               {
                   role: "user",
                   content: `Break down this task into key components: ${task}\n\nRespond with a JSON array of strings, like: ["Step 1: ...", "Step 2: ...", ...]`
               }
           ],
       });
       
       const content = response.data.choices[0].message.content;
       const components = JSON.parse(content);
       return components;
   }
   ```

### Option 2: Anthropic Claude

1. Install Anthropic package:
   ```bash
   npm install @anthropic-ai/sdk
   ```

2. Get an API key from [Anthropic](https://console.anthropic.com/)

3. Update the `decomposeWithAI` method:

   ```typescript
   private async decomposeWithAI(task: string): Promise<string[]> {
       const Anthropic = require("@anthropic-ai/sdk");
       
       const client = new Anthropic({
           apiKey: process.env.ANTHROPIC_API_KEY,
       });
       
       const message = await client.messages.create({
           model: "claude-3-sonnet-20240229",
           max_tokens: 1024,
           messages: [
               {
                   role: "user",
                   content: `Break down this task into 3-5 specific, actionable steps. Respond with a JSON array of strings: ${task}`
               }
           ],
       });
       
       const content = message.content[0].type === 'text' ? message.content[0].text : '';
       const jsonMatch = content.match(/\[.*\]/s);
       const components = JSON.parse(jsonMatch[0]);
       return components;
   }
   ```

### Option 3: Local/Custom API

Replace the `decomposeWithAI` method to call your own API endpoint:

```typescript
private async decomposeWithAI(task: string): Promise<string[]> {
    const response = await fetch('http://your-api.com/decompose', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task })
    });
    
    const data = await response.json();
    return data.components;
}
```

## Development

### Build Commands

```bash
# Watch mode (auto-compile on changes)
npm run esbuild-watch

# Production build
npm run vscode:prepublish

# Type checking
npm run compile

# Linting
npm run lint
```

### Debug

1. Press `F5` to start debugging
2. This opens a new VS Code window with the extension loaded
3. Set breakpoints in the code and interact with the extension
4. Changes to TypeScript files require restarting the debug session

### File Structure

```
.
├── src/
│   └── extension.ts          # Main extension code
├── media/
│   └── icon.svg              # Activity bar icon
├── package.json              # Extension manifest
├── tsconfig.json             # TypeScript config
└── README.md                 # This file
```

## Configuration

You can customize the extension by adding configuration options to `package.json`:

```json
"contributes": {
  "configuration": {
    "title": "Task Decomposer",
    "properties": {
      "taskDecomposer.timerDuration": {
        "type": "number",
        "default": 3,
        "description": "Focus timer duration in seconds"
      },
      "taskDecomposer.apiKey": {
        "type": "string",
        "description": "API key for AI service"
      }
    }
  }
}
```

## Known Limitations

- Currently shows a placeholder component list without actual AI decomposition (requires API integration)
- Timer is hardcoded to 3 seconds
- No persistence of task history or components

## Future Enhancements

- [ ] Save task history to workspace storage
- [ ] Configurable timer duration
- [ ] Multiple AI provider support with easy switching
- [ ] Component notes and progress tracking
- [ ] Pomodoro timer integration
- [ ] Command palette integration
- [ ] Custom task templates

## Troubleshooting

### Extension doesn't appear in activity bar

- Make sure you've installed and built the extension (`npm install && npm run esbuild`)
- Reload VS Code (`Cmd+R` or `Ctrl+Shift+F5`)

### API calls failing

- Verify your API key is set correctly as an environment variable
- Check the VS Code output panel for error messages
- Ensure you have internet connectivity

### Timer not working

- Check browser console (F12 in the webview) for JavaScript errors
- Make sure the message API communication is working properly

## Support

For issues, feature requests, or contributions, please open an issue or pull request on GitHub.

## License

MIT
