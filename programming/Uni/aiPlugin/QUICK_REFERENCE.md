# Task Decomposer - Quick Reference

## ⚡ Quick Start

```powershell
# 1. Navigate to project
cd C:\Users\Brian\ Geisler\OneDrive\programming\Uni\aiPlugin

# 2. Install dependencies
npm install

# 3. Build
npm run esbuild

# 4. Run (press F5 in VS Code with this folder open)
# Wait for new window to open with extension

# 5. In the extension window, click the icon in the left sidebar
```

## 📁 Project Files

| File | Purpose |
|------|---------|
| `src/extension.ts` | Main logic - **Edit this to add AI** |
| `package.json` | Configuration & dependencies |
| `tsconfig.json` | TypeScript settings |
| `media/icon.svg` | Sidebar icon |
| `README.md` | Full documentation |
| `SETUP.md` | Setup walkthrough |
| `PROJECT_OVERVIEW.md` | Architecture & file explanations |
| `AI_INTEGRATION_EXAMPLES.md` | Copy-paste AI code |

## 🛠️ Development Commands

```powershell
npm run esbuild              # Build for production
npm run esbuild-watch       # Auto-rebuild on changes
npm run compile             # Type check
npm run lint                # Check code style
npm run vscode:prepublish   # Minified production build
```

## 🔑 Environment Setup

### Prerequisites
- [ ] Node.js installed (nodejs.org)
- [ ] VS Code latest version
- [ ] This project folder opened in VS Code

### Run the Extension
1. Open this folder in VS Code
2. Press `F5`
3. New window opens with extension
4. Click the icon in left sidebar

### Debugging
- Set breakpoints in `src/extension.ts`
- Changes require rebuild (`npm run esbuild`) + reload (`Ctrl+Shift+R`)
- View logs in "Output" panel → select "Task Decomposer"

## 🤖 Add AI Integration

### Step 1: Choose Service
- **OpenAI** (ChatGPT) ← Recommended
- **Anthropic** (Claude)
- **Google** (Gemini)
- **Local** (Ollama)
- **Custom** API

### Step 2: Get API Key
| Service | Where |
|---------|-------|
| OpenAI | platform.openai.com/api-keys |
| Anthropic | console.anthropic.com |
| Google | makersuite.google.com/app/apikey |
| Ollama | ollama.ai (free, local) |

### Step 3: Set Environment Variable (PowerShell)
```powershell
$env:OPENAI_API_KEY = "your-key-here"
# Or for Anthropic:
$env:ANTHROPIC_API_KEY = "your-key-here"
```

### Step 4: Install Package
```powershell
# For OpenAI
npm install openai

# For Anthropic
npm install @anthropic-ai/sdk

# For Google Gemini
npm install @google/generative-ai
```

### Step 5: Copy & Paste Code
1. Open `AI_INTEGRATION_EXAMPLES.md`
2. Find your service
3. Copy the function
4. Open `src/extension.ts`
5. Find `decomposeWithAI()` method (line ~175)
6. **Replace entire method** with copied code

### Step 6: Rebuild & Test
```powershell
npm run esbuild
# Press Ctrl+Shift+R in extension window
# Try decomposing a task
```

## 🎨 Customize UI

### Change Timer (seconds)
In `src/extension.ts`, line ~40:
```typescript
private timerCount: number = 3;  // ← Change 3 to anything
```

### Change Sidebar Icon
Replace `media/icon.svg` with your SVG file

### Change Panel Name
In `package.json`, line ~28:
```json
"title": "Task Decomposer"  // ← Change this
```

### Change Colors/Layout
In `src/extension.ts`, find `getHtmlContent()` → edit the `<style>` section

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| `npm: not found` | Install Node.js, restart VS Code |
| Extension doesn't appear | Run `npm install` then `npm run esbuild` |
| Timer doesn't show | Check VS Code output panel for errors |
| AI returns errors | Check env var is set: `$env:OPENAI_API_KEY` |
| Changes don't show | Rebuild (`npm run esbuild`), then reload (`Ctrl+Shift+R`) |

## 📦 Share Your Extension

```powershell
npm install -g vsce
vsce package
# Creates task-decomposer-0.0.1.vsix
# Share this file!
```

## 🎯 Feature Checklist

- [x] Sidebar button
- [x] Task input
- [x] Components list
- [x] 3-second timer
- [ ] AI integration (you add this!)
- [ ] Save history (optional enhancement)
- [ ] Configurable timer (optional enhancement)
- [ ] Keyboard shortcuts (optional enhancement)

## 📚 Learn More

- **VS Code API**: code.visualstudio.com/api
- **Webview Guide**: code.visualstudio.com/api/extension-guides/webview
- **Extension Samples**: github.com/microsoft/vscode-extension-samples

---

**Version**: 0.0.1  
**Status**: Ready for AI integration! 🚀
