# Advanced Setup Guide

## System Requirements

- **Node.js**: v16 or higher
- **npm**: v8 or higher
- **Chrome/Edge/Brave**: Latest version
- **RAM**: 4GB recommended (for Ollama)
- **Disk Space**: 5GB for Ollama + models

## Detailed Installation Steps

### Step 1: Prepare Your System

#### Windows
1. Download and install Node.js from https://nodejs.org/
2. Open PowerShell and verify:
   ```powershell
   node --version
   npm --version
   ```

#### macOS
```bash
# Using Homebrew
brew install node

# Or download from https://nodejs.org/
node --version
npm --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install nodejs npm

node --version
npm --version
```

### Step 2: Install Ollama

#### Windows
1. Download: https://ollama.ai/download/windows
2. Run the installer
3. Ollama will start automatically
4. Open Command Prompt and run:
   ```cmd
   ollama pull llama2
   ```

#### macOS
1. Download: https://ollama.ai/download/mac
2. Drag to Applications
3. Launch Ollama
4. Open Terminal and run:
   ```bash
   ollama pull llama2
   ```

#### Linux
```bash
curl https://ollama.ai/install.sh | sh
ollama pull llama2
```

**Verify Ollama is running:**
```bash
curl http://localhost:11434/api/tags
```

You should see a JSON response with available models.

### Step 3: Clone and Setup Extension

```bash
# Navigate to the programming folder
cd c:/Users/Brian Geisler/gitSynced/main/programming

# Navigate to extension folder
cd Uni/aiBrowserPlugin/extension

# Install dependencies
npm install

# Build for production
npm run build

# Or development (watch mode)
npm run dev
```

### Step 4: Load Extension in Chrome

1. **Open Chrome** (or Edge, Brave)
2. Go to: `chrome://extensions/`
3. Toggle **Developer Mode** (top right corner)
4. Click **Load unpacked**
5. Navigate to: `c:/Users/Brian Geisler/gitSynced/main/programming/Uni/aiBrowserPlugin/extension/dist`
6. Click **Select Folder**

✅ Extension is now installed!

## Troubleshooting

### Build Issues

**Error: "Cannot find module 'webpack'"**
```bash
npm install --save-dev webpack webpack-cli
npm run build
```

**Error: "TypeScript not found"**
```bash
npm install --save-dev typescript ts-loader
npm run build
```

### Ollama Issues

**Ollama not responding**
- Restart Ollama application
- Windows: Check system tray, restart if needed
- macOS: Quit and reopen from Applications
- Linux: `sudo systemctl restart ollama`

**Model not found**
```bash
ollama list
ollama pull llama2
```

**Port already in use (11434)**
- Change Ollama port: `OLLAMA_HOST=localhost:11435 ollama serve`
- Update [src/utils/aiTaskBreakdown.ts](src/utils/aiTaskBreakdown.ts) to use new port

### Extension Issues

**Extension not loading**
- Hard refresh Chrome: Ctrl+Shift+R (or Cmd+Shift+R on Mac)
- Disable and re-enable extension
- Delete dist folder and rebuild: `npm run build`

**Floating button not appearing**
- Refresh the webpage: F5 or Ctrl+R
- Check extension is enabled in chrome://extensions/
- Try on a different website

**Task breakdown fails**
- Check browser console for errors (F12 → Console)
- Verify Ollama is running: `http://localhost:11434`
- Try the fallback (no AI) by entering a simple task

## Performance Optimization

### For Faster Task Breakdown

1. **Use faster Ollama model**:
   ```bash
   ollama pull mistral  # Faster than llama2
   ```
   Then update [aiTaskBreakdown.ts](src/utils/aiTaskBreakdown.ts):
   ```typescript
   model: 'mistral'  // Change from llama2
   ```

2. **Reduce model context**:
   In `aiTaskBreakdown.ts`, lower the prompt complexity

### For Better Performance

- Close other browser tabs
- Stop other Ollama operations
- Ensure at least 2GB free RAM

## Development Workflow

### Watch Mode (Auto-rebuild)
```bash
npm run dev
```
Changes are automatically compiled to `dist/`

### Manual Build
```bash
npm run build
```

### After Making Changes

1. Save your file
2. If in dev mode, webpack auto-compiles
3. In Chrome, click reload button on extension card in chrome://extensions/
4. Refresh the webpage with Ctrl+R

## Configuration

### Changing AI Provider

Edit [src/utils/aiTaskBreakdown.ts](src/utils/aiTaskBreakdown.ts):

1. Replace `breakdownWithOllama` with your provider
2. Update manifest.json if needed for API permissions
3. Rebuild: `npm run build`

### Customizing UI

Edit files in `src/popup/styles/`:
- `popup.css` - Main layout
- `task-input.css` - Input form
- `task-list.css` - Task list
- `subtask-row.css` - Subtask rows
- `timer.css` - Timer display

### Modifying Storage

Edit `src/utils/storage.ts` to change storage behavior.

## Advanced: Using Alternative Models

Instead of Ollama, you can use:

### Option 1: HuggingFace Inference API (Free tier available)
```typescript
const response = await fetch('https://api-inference.huggingface.co/models/gpt2', {
  headers: { Authorization: 'Bearer YOUR_TOKEN' },
  method: 'POST',
  body: JSON.stringify({ inputs: prompt }),
});
```

### Option 2: Local Transformers.js (No backend needed)
Install: `npm install @xenova/transformers`

### Option 3: Self-hosted LLaMA
Run your own LLaMA server on any port

## Deployment Considerations

When deploying to Chrome Web Store:
1. Update manifest.json version
2. Create privacy policy
3. Ensure no hardcoded API keys
4. Test thoroughly

## Support & Resources

- **Ollama Help**: https://ollama.ai
- **Chrome Extension Docs**: https://developer.chrome.com/docs/extensions/
- **React Docs**: https://react.dev
- **TypeScript Docs**: https://www.typescriptlang.org/docs/

## Next Steps

1. Read [README.md](./README.md) for feature overview
2. Try the [QUICKSTART.md](./QUICKSTART.md) if you haven't yet
3. Start using the extension!
