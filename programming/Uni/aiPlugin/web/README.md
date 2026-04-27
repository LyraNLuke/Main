# Task Decomposer - Web Version

A browser-based task decomposition app with AI-powered analysis and focus timer.

## Features

- 🤖 **AI-Powered Task Breakdown** - Break down any task into 3-5 actionable steps
- ⏱️ **Focus Timer** - 3-second countdown to help you get into focus
- 📋 **Component Tracking** - Work through each component step-by-step
- 💾 **Local Storage** - Saves API keys and task history locally (browser only)
- 🌐 **Works Offline** - No server needed, runs entirely in browser
- 🎨 **Modern UI** - Dark theme designed for focus

## Quick Start

### 1. Open in Browser

Simply open `index.html` in your web browser, or access it via a local server:

```bash
# Using Python 3
python -m http.server 8000

# Using Python 2
python -m SimpleHTTPServer 8000

# Using Node.js (if installed)
npx http-server

# Using PHP
php -S localhost:8000
```

Then open: `http://localhost:8000`

### 2. Setup AI (Optional)

The app works with or without API setup:

**Without API:**
- Click "Skip for Now" on setup screen
- Tasks are broken down using generic steps
- Works completely offline

**With AI API:**
Choose one of these services:

#### Option A: OpenAI (ChatGPT) - Recommended
1. Go to https://platform.openai.com/api-keys
2. Create an account or sign in
3. Generate a new API key
4. Paste it into the app

**Cost:** Pay-as-you-go (~$0.001 per task)

#### Option B: Anthropic Claude
1. Go to https://console.anthropic.com
2. Create an account or sign in
3. Generate an API key
4. Paste it into the app

**Cost:** Pay-as-you-go

#### Option C: Google Gemini
1. Go to https://makersuite.google.com/app/apikey
2. Sign in with Google
3. Create API key (free tier available)
4. Paste it into the app

**Cost:** Free tier available, then pay-as-you-go

### 3. Use It!

1. Click "New Task" button
2. Enter a task you want to break down
3. Click "Decompose Task"
4. Click "Start" on any component
5. Get ready during the 3-second countdown
6. Start working on that component

## File Structure

```
web/
├── index.html           # Main HTML structure
├── styles.css           # UI styling
├── config.js            # Configuration & storage
├── ai-service.js        # AI API integrations
├── app.js              # Application logic
└── README.md           # This file
```

## How It Works

### Architecture

```
User Opens Browser
    ↓
index.html loads (HTML/CSS/JavaScript)
    ↓
App checks localStorage for API key
    ↓
If API configured: Go to task input
If not: Show welcome screen
    ↓
User enters task
    ↓
JavaScript calls AI API (CORS request)
    ↓
Components displayed in browser
    ↓
User clicks "Start" on component
    ↓
3-second timer countdown in JavaScript
    ↓
User ready to start working
```

### Storage

All data stored **locally in browser only**:
- API keys
- Task history (last 20 tasks)
- No data sent to any server (except AI services)

### Security Note

API keys are stored in browser's `localStorage`. This is:
- **Safe for personal use** ✅
- **Not recommended for shared computers** ⚠️
- **Not recommended for enterprise** ⚠️

For shared environments, clear localStorage before closing:
```javascript
localStorage.clear()
```

## AI Integration Details

### How CORS Works

When you call AI services from the browser:

1. Browser makes CORS request to AI service
2. AI service receives your API key and request
3. AI service responds with decomposed task
4. Response displayed in browser
5. **Your API key never touches your server**

**Note:** This means API costs are incurred on **your account**, not the app creator's.

### Supported Services

| Service | Free Tier | Setup Time | Quality |
|---------|-----------|-----------|---------|
| OpenAI | No | 5 min | Excellent |
| Claude | No | 5 min | Excellent |
| Gemini | Yes | 5 min | Good |
| Placeholder | Yes | 0 min | Basic |

### Usage Costs Estimate

All are pay-as-you-go. Estimated cost per task decomposition:

| Service | Cost/Task |
|---------|-----------|
| OpenAI | ~$0.0005-0.001 |
| Claude | ~$0.001-0.002 |
| Gemini | ~$0.0001-0.0005 |

(Based on typical task input sizes)

## Configuration

All configuration is in browser localStorage. No config files to edit.

### Change Timer Duration

Edit in `app.js`, line ~137:
```javascript
this.timerCount = 3;  // Change 3 to desired seconds
```

Then refresh browser.

### Change UI Colors

Edit in `styles.css`:
```css
:root {
	--color-primary: #0e639c;
	--color-text: #e0e0e0;
	/* ... other colors ... */
}
```

## Troubleshooting

### "API Error" when decomposing

**Solution:**
1. Check API key is correct
2. Check you have API credits remaining
3. Check internet connection
4. Try different API service

### Timer not showing

**Solution:**
1. Refresh page
2. Clear browser cache (Ctrl+Shift+Delete)
3. Try different browser

### Forgot API key

**Solution:**
1. Click "New Task"
2. In browser console, run: `localStorage.clear()`
3. Refresh page
4. Re-enter new API key

### Tasks not saving

**Solution:**
1. Check if localStorage is enabled in browser
2. Try private/incognito window
3. Check browser storage limits (usually 5-10MB)

## Deployment Options

### Option 1: Own Server
```bash
# Copy web/ folder to your server
# Serve via HTTP/HTTPS
```

### Option 2: GitHub Pages
```bash
# Push to GitHub
# Enable GitHub Pages in repo settings
# App accessible at: https://username.github.io/repo
```

### Option 3: Netlify (Free)
1. Push code to GitHub
2. Connect GitHub repo to Netlify
3. App deploys automatically

### Option 4: Vercel (Free)
1. Push code to GitHub
2. Import project in Vercel
3. App deployed instantly

## Advanced: Custom AI Service

To use your own AI backend, edit `ai-service.js`:

```javascript
async decompose(task) {
	const response = await fetch('YOUR_BACKEND_URL', {
		method: 'POST',
		body: JSON.stringify({ task })
	});
	
	const data = await response.json();
	return data.components;
}
```

Your backend should:
- Accept POST request with `task` parameter
- Return JSON: `{ "components": ["step 1", "step 2", ...] }`
- Handle CORS headers

## Browser Support

| Browser | Support |
|---------|---------|
| Chrome | ✅ Full |
| Firefox | ✅ Full |
| Safari | ✅ Full |
| Edge | ✅ Full |
| IE 11 | ❌ No |

## Privacy

- **API keys:** Stored locally in your browser
- **Tasks:** Stored locally in your browser localStorage
- **Data sent to:** Only the AI service API (OpenAI, Claude, Gemini)
- **No tracking:** No analytics or tracking code

## Future Ideas

- [ ] Dark/Light theme toggle
- [ ] Keyboard shortcuts
- [ ] Export tasks to PDF
- [ ] Voice input for tasks
- [ ] Real-time collaboration
- [ ] Mobile app version
- [ ] Integration with calendars
- [ ] Multiple language support

## License

MIT - Feel free to use, modify, and distribute

## Support

For issues or feature requests, check:
1. Browser console for errors (F12)
2. This README troubleshooting section
3. Open an issue on GitHub

---

**Enjoy breaking down your tasks!** 🚀
