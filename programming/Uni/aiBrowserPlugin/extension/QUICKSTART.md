# Quick Start Guide

Get the AI Task Breakdown Assistant running in 5 minutes!

## 1. Install Ollama (1 minute)

- Download from: https://ollama.ai
- Install and run
- In terminal: `ollama pull llama2`

## 2. Build Extension (2 minutes)

```bash
cd extension
npm install
npm run build
```

## 3. Load in Chrome (1 minute)

1. Go to `chrome://extensions/`
2. Enable Developer Mode (top right)
3. Click "Load unpacked"
4. Select `extension/dist/` folder

## 4. Start Using! (1 minute)

1. Make sure Ollama is running in background
2. Go to any website
3. Click the purple button (bottom right)
4. Enter your task
5. Click "Break Down Task"
6. Start working! ⏱️

## Troubleshooting

**"Failed to break down task"?**
- Make sure Ollama is running: `ollama serve`
- Check: http://localhost:11434
- Model pulled: `ollama pull llama2`

**Button not appearing?**
- Reload the webpage (Ctrl+R)
- Check extension is enabled in chrome://extensions/

**Build errors?**
- Delete node_modules: `rm -rf node_modules`
- Reinstall: `npm install`
- Rebuild: `npm run build`

## Next Steps

- Read [README.md](./README.md) for full documentation
- Check [Advanced Setup](./SETUP.md) for customization
