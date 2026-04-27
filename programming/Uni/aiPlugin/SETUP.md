# Setup Guide for Task Decomposer

## What You Need to Know

Your Task Decomposer extension is ready! Here's how to get it running.

## Quick Start (No AI yet)

### 1. Install Node.js

If you haven't already:
- Download from [nodejs.org](https://nodejs.org/) - choose the LTS version
- Install it (restart your terminal after installation)

### 2. Build the Extension

Open a Terminal and navigate to your aiPlugin folder:

```powershell
cd C:\Users\Brian\ Geisler\OneDrive\programming\Uni\aiPlugin
npm install
npm run esbuild
```

This downloads dependencies and builds the extension.

### 3. Run in VS Code

1. Open the `aiPlugin` folder in VS Code
2. Press `F5` to launch the extension in debug mode
3. A new VS Code window will open with the extension active
4. Look for the icon in the left activity bar (should say "Task Decomposer")

### 4. Try It Out

1. Click the Task Decomposer icon
2. Click "Start New Task"
3. Enter a task (e.g., "Build a website")
4. You'll see placeholder components
5. Click "Start" on any component to see the 3-second timer

## Adding AI Integration

Currently, the extension breaks tasks into generic steps. To use real AI:

### Choose Your AI Service

Pick one:
- **OpenAI** (ChatGPT) - Recommended for quality
- **Anthropic** (Claude) - Great alternative
- **Your own API** - Full control

### Steps for OpenAI

1. **Get API Key**
   - Go to https://platform.openai.com/api-keys
   - Create an account if needed
   - Generate a new API key
   - Copy it somewhere safe

2. **Install OpenAI Package**
   ```powershell
   cd C:\Users\Brian\ Geisler\OneDrive\programming\Uni\aiPlugin
   npm install openai
   ```

3. **Set Environment Variable** (Windows PowerShell)
   ```powershell
   $env:OPENAI_API_KEY = "your-api-key-here"
   ```

4. **Update the Code**
   - Open `src/extension.ts` in VS Code
   - Find the `decomposeWithAI` method (around line 175)
   - Replace it with the OpenAI code from the README

5. **Rebuild**
   ```powershell
   npm run esbuild
   ```

6. **Test**
   - Press `F5` to run again
   - Try decomposing a task

## Common Issues

### npm not found
- Node.js isn't installed or not in PATH
- Restart VS Code and try again after installing Node.js

### "Cannot find module"
- Run `npm install` in the aiPlugin folder

### Timer not showing
- Make sure you're in the VS Code extension window (not your main window)
- Reload the webview by closing and reopening the panel

### API errors
- Check that your API key is correct
- Verify you have internet connection
- Check VS Code's output panel for error details

## File Structure

```
aiPlugin/
├── src/
│   └── extension.ts          ← Main code (edit this for AI integration)
├── media/
│   └── icon.svg              ← Sidebar icon
├── package.json              ← Dependencies and config
├── tsconfig.json             ← TypeScript settings
├── README.md                 ← Full documentation
└── SETUP.md                  ← This file
```

## Next Steps

1. ✅ Build and run the extension locally
2. ⏳ Integrate with an AI service of your choice
3. 🚀 Customize the UI and timer
4. 📦 Package and share your extension

## Commands Useful During Development

```powershell
# Watch for changes (auto-rebuild)
npm run esbuild-watch

# Production build (minified)
npm run vscode:prepublish

# Check for TypeScript errors
npm run compile

# Lint code for issues
npm run lint
```

## Need Help?

1. Check the README.md for more details
2. Look at the VS Code Extension samples: https://github.com/microsoft/vscode-extension-samples
3. VS Code API docs: https://code.visualstudio.com/api

Good luck! 🚀
