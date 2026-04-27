# Browser Version - Quick Start

Perfect! Your browser version is ready. Here's everything you need to know.

## 🎯 What You Have

A complete web app that:
- Works in any browser (Chrome, Firefox, Safari, Edge)
- Breaks down tasks using AI
- Shows a 3-second timer before each component
- Stores everything locally (no server needed)
- Works offline with placeholder mode

## ⚡ Get Running in 30 Seconds

### On Windows:

```powershell
# 1. Navigate to the web folder
cd "c:\Users\Brian Geisler\OneDrive\programming\Uni\aiPlugin\web"

# 2. Start a simple server (Python 3)
python -m http.server 8000

# 3. Open in browser
start http://localhost:8000
```

Or just **double-click** `index.html` to open directly in your browser (no server needed!).

### On Mac/Linux:

```bash
cd ~/OneDrive/programming/Uni/aiPlugin/web
python3 -m http.server 8000
# Then go to http://localhost:8000
```

## 📁 Files

```
web/
├── index.html         ← Main page (open this!)
├── styles.css         ← Beautiful dark UI
├── config.js          ← Storage management
├── ai-service.js      ← AI integrations
├── app.js            ← Application logic
└── README.md         ← Full documentation
```

## 🤖 AI Integration (Choose One)

### Easiest: Skip Setup
- Click "Skip for Now" on start
- Tasks broken down generically
- Works 100% offline
- **Cost:** FREE

### Best Quality: OpenAI (ChatGPT)
1. Go: https://platform.openai.com/api-keys
2. Get API key (takes 2 min)
3. Select "OpenAI" in app
4. Paste key
5. Done!
- **Cost:** ~$0.0005 per task

### Alternative: Google Gemini
1. Go: https://makersuite.google.com/app/apikey
2. Get API key (free tier available)
3. Select "Gemini" in app
4. Paste key
5. Done!
- **Cost:** Free or pay-as-you-go

### Alternative: Anthropic Claude
1. Go: https://console.anthropic.com
2. Get API key
3. Select "Claude" in app
4. Paste key
5. Done!
- **Cost:** Pay-as-you-go

## 🎮 Using the App

1. **Open** `index.html` or go to `http://localhost:8000`
2. **Click** "Get Started" (or "Skip for Now" to use without AI)
3. **Enter** a task (e.g., "Build a website", "Learn Python")
4. **Click** "Decompose Task"
5. **See** the components
6. **Click** "Start" on any component
7. **Watch** the 3-second timer countdown
8. **Start** working when ready

## 💾 Storage

Everything saved locally in your browser:
- API key (if you set one)
- Last 20 tasks (for history)
- No internet needed to use

**To clear everything:**
- Open browser console (F12)
- Type: `localStorage.clear()`
- Refresh

## 🔧 Customization

### Change Timer (seconds)
In `app.js`, find line ~137:
```javascript
this.timerCount = 3;  // Change 3 to any number
```

### Change Colors
In `styles.css`, edit:
```css
:root {
	--color-primary: #0e639c;       /* Main button color */
	--color-text: #e0e0e0;          /* Text color */
	--color-bg: #1e1e1e;            /* Background */
}
```

### Different AI Service
Already built-in! Just select during setup.

## 📊 How It Works

```
User opens browser
  ↓
App loads from HTML/CSS/JavaScript
  ↓
Check for saved API key
  ↓
User enters task
  ↓
App calls AI API (if configured)
  ↓
AI returns task components
  ↓
Displayed in browser
  ↓
User clicks "Start"
  ↓
3-second timer counts down
  ↓
User ready to work!
```

## 🌐 Deploy to Internet

Want to share with others? Two options:

### Option 1: GitHub Pages (Free)
1. Push `web/` folder to GitHub
2. Enable GitHub Pages
3. Share link: `https://username.github.io/repo`

### Option 2: Netlify (Free)
1. Connect GitHub to Netlify
2. Deploys automatically
3. Gets a live URL

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Browser won't open file | Use `python -m http.server 8000` instead |
| API key error | Check key is correct, have credits remaining |
| Timer not showing | F5 to refresh, Ctrl+Shift+Delete to clear cache |
| Nothing happens | Open F12 (Developer Tools), check Console for errors |

## 📚 More Info

- Full docs: [README.md](README.md)
- Main project: [../../INDEX.md](../../INDEX.md)
- VS Code extension: [../../README.md](../../README.md)

## ✨ What's Different from VS Code Version

| Feature | Browser | VS Code |
|---------|---------|---------|
| Setup | None needed | Node.js required |
| AI integration | Built-in options | Needs manual setup |
| Storage | Browser localStorage | VS Code workspace |
| Deployment | Share URL | Install from marketplace |
| Offline mode | Yes | Yes |

---

**Ready?** Open `index.html` now! 🚀

Need help? Check README.md for detailed docs.
