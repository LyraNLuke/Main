# Getting Started Checklist ✅

Complete these steps in order to get the AI Browser Plugin working!

## Phase 1: System Setup (5-10 minutes)

- [ ] **Install Node.js**
  - Download from https://nodejs.org/
  - Verify: Open terminal/PowerShell and run `node --version` and `npm --version`
  
- [ ] **Install Ollama (for AI)**
  - Download from https://ollama.ai
  - Install and run the application
  - Verify Ollama is running (should appear in system tray/menu bar)

- [ ] **Download Ollama Model**
  - Open terminal/PowerShell/command prompt
  - Run: `ollama pull llama2` (this may take 5-10 minutes)
  - Verify: Run `ollama list` to see installed models

## Phase 2: Build Extension (2-3 minutes)

- [ ] **Navigate to extension folder**
  ```
  Windows: cd c:\Users\Brian Geisler\gitSynced\main\programming\Uni\aiBrowserPlugin\extension
  Mac/Linux: cd ~/gitSynced/main/programming/Uni/aiBrowserPlugin/extension
  ```

- [ ] **Install dependencies**
  - Run: `npm install`
  - Wait for it to complete (may take 1-2 minutes)

- [ ] **Build the extension**
  - Run: `npm run build`
  - Check that a `dist/` folder was created

## Phase 3: Load in Chrome (2-3 minutes)

- [ ] **Open Chrome Extension Manager**
  - Open Chrome browser
  - Go to: `chrome://extensions/` (type this in address bar)

- [ ] **Enable Developer Mode**
  - Look for toggle in top-right corner
  - Click to enable (it should turn on)

- [ ] **Load Extension**
  - Click "Load unpacked" button
  - Navigate to: `c:\Users\Brian Geisler\gitSynced\main\programming\Uni\aiBrowserPlugin\extension\dist`
  - Select the `dist` folder
  - Click "Select Folder"

- [ ] **Verify Extension Loaded**
  - You should see the extension in the list
  - It should say "AI Task Breakdown Assistant"
  - Click the extension icon to see options

## Phase 4: Test It! (5 minutes)

- [ ] **Make sure Ollama is running**
  - Keep Ollama app open
  - Verify by going to: http://localhost:11434 in browser
  - You should see Ollama response

- [ ] **Open any website**
  - Go to Google, YouTube, any website
  - Look for a **purple button with a checkmark** in the bottom-right corner

- [ ] **Click the floating button**
  - Click the purple button
  - A popup should open

- [ ] **Enter a task**
  - Click in the text area
  - Type a task like: "Learn Python programming"
  - Click "Break Down Task"

- [ ] **Wait for AI breakdown**
  - The AI should break it into smaller tasks
  - You should see: Research, Setup, Learn, Practice, etc.

- [ ] **Test the timer**
  - Click on one of the subtasks
  - Click "Start Task"
  - You should see a countdown from 5
  - Then a stopwatch should start automatically
  - Click "Mark Done" when finished

- [ ] **Minimize and check**
  - Collapse the popup
  - Hover over the floating button
  - It should show the current task name and time spent

## 🎉 You're Done!

The extension is now working! Here's what you can do next:

### Quick Tips
- Keep Ollama running in the background while using the extension
- The floating button is draggable - you can move it around
- Tasks are saved automatically
- Restart Chrome to see updated extension

### Troubleshooting

**Problem: "Failed to break down task"**
- [ ] Is Ollama running? (Check system tray)
- [ ] Did you run `ollama pull llama2`?
- [ ] Is it on port 11434?

**Problem: Button not appearing**
- [ ] Reload the webpage (Ctrl+R or Cmd+R)
- [ ] Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
- [ ] Check extension is enabled: chrome://extensions/

**Problem: Build errors**
- [ ] Delete `node_modules` folder
- [ ] Run `npm install` again
- [ ] Run `npm run build` again

## Next Steps

1. **Read the docs**
   - [README.md](./README.md) - Full feature documentation
   - [PROJECT_OVERVIEW.md](./PROJECT_OVERVIEW.md) - How it all works

2. **Customize (Optional)**
   - Edit CSS files in `src/popup/styles/`
   - Change colors, fonts, layout

3. **Use Regularly**
   - Open the extension on any webpage
   - Break down your tasks
   - Track your time
   - Build better habits!

## Common Issues by OS

### Windows
- **Ollama not found**: Make sure you installed it properly. Check Start menu for Ollama.
- **PowerShell permission denied**: Try using Command Prompt (cmd.exe) instead
- **Port 11434 in use**: Something else is using it. Restart your computer.

### macOS
- **Ollama quit unexpectedly**: Relaunch it from Applications
- **Command not found**: You might need to restart Terminal after installing
- **Port 11434 in use**: Run `sudo lsof -i :11434` to find what's using it

### Linux
- **Ollama command not found**: Might need to add to PATH. Try: `~/.ollama/bin/ollama`
- **Permission denied**: Run with sudo or fix permissions
- **Out of memory**: Ollama can use 2-4GB. Check available RAM.

## Still Stuck?

Check these files for detailed help:
- [QUICKSTART.md](./QUICKSTART.md) - 5-minute quick start
- [SETUP.md](./SETUP.md) - Detailed advanced setup
- [PROJECT_OVERVIEW.md](./PROJECT_OVERVIEW.md) - How it all works

Good luck! 🚀
