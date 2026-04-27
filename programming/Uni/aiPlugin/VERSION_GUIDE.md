# Task Decomposer - Choose Your Version

Welcome! You now have **two versions** to choose from:

## 📱 Browser Version (NEW!) ⭐ RECOMMENDED FOR MOST PEOPLE

**Perfect if you want:** Easy setup, quick to start, works everywhere

- ✅ No installation needed
- ✅ Works in any browser
- ✅ Built-in AI options (Google, OpenAI, Claude)
- ✅ Works offline (with placeholder mode)
- ✅ Local storage only (privacy)
- ✅ Share with URL (deploy to internet easily)
- ✅ Mobile friendly

### Get Started
→ **Go to** [`web/QUICK_START.md`](web/QUICK_START.md)

### Full Documentation
→ **Read** [`web/README.md`](web/README.md)

### AI Setup Guide
→ **Follow** [`web/AI_SETUP_GUIDE.md`](web/AI_SETUP_GUIDE.md)

---

## 🔧 VS Code Extension (ADVANCED)

**Perfect if you want:** Integration with VS Code, development setup, enterprise deployment

- ✅ Sidebar button in VS Code
- ✅ Runs inside VS Code
- ✅ Full TypeScript support
- ✅ Can be packaged for distribution
- ⚠️ Requires Node.js installation
- ⚠️ Build step needed
- ⚠️ More complex setup

### Get Started
→ **Go to** [`SETUP.md`](SETUP.md)

### Full Documentation
→ **Read** [`README.md`](README.md)

---

## 🎯 Quick Decision

| Question | Answer | Use |
|----------|--------|-----|
| Want quickest setup? | Yes | Browser ✅ |
| Want to use in VS Code? | Yes | VS Code |
| Have Node.js installed? | No | Browser ✅ |
| Need to share with others? | Yes | Browser ✅ |
| Want to build an extension? | Yes | VS Code |
| Want 100% offline? | Yes | Browser (placeholder mode) ✅ |
| Want best AI quality? | Yes | Browser ✅ (with OpenAI) |

---

## 🚀 Recommended Path

### For 95% of Users:

1. **Start**: Go to `web/` folder
2. **Open**: `index.html` in browser
3. **Click**: "Get Started"
4. **Choose AI**: "Skip for Now" or pick one (5 min setup)
5. **Use**: Enter a task, get components, use timer

**Time to first use:** 2-5 minutes

### For VS Code Users:

1. **Read**: `SETUP.md`
2. **Install**: Node.js
3. **Run**: `npm install && npm run esbuild`
4. **Press**: F5 to test
5. **Setup AI**: Follow `AI_INTEGRATION_EXAMPLES.md`

**Time to first use:** 15-30 minutes

---

## 📂 Project Structure

```
aiPlugin/
├── web/                           ← BROWSER VERSION START HERE!
│   ├── index.html                 ← Open this in browser
│   ├── styles.css                 ← UI styling
│   ├── app.js                     ← Main logic
│   ├── ai-service.js              ← AI integrations
│   ├── config.js                  ← Storage
│   ├── QUICK_START.md             ← 2-minute guide
│   ├── README.md                  ← Full docs
│   └── AI_SETUP_GUIDE.md          ← AI setup
│
├── src/                           ← VS CODE EXTENSION
│   └── extension.ts               ← VS Code plugin code
│
├── media/
│   └── icon.svg
│
├── SETUP.md                       ← VS Code setup guide
├── README.md                      ← VS Code full docs
├── AI_INTEGRATION_EXAMPLES.md     ← VS Code AI setup
├── QUICK_REFERENCE.md             ← VS Code cheat sheet
└── INDEX.md                       ← THIS FILE
```

---

## 🎓 Understanding the Two Versions

### Browser Version

```
You open index.html
    ↓
HTML/CSS/JavaScript loads in browser
    ↓
App runs 100% in your browser
    ↓
API keys stored in browser localStorage only
    ↓
Call AI services from browser (if configured)
    ↓
Works offline or with AI
```

**Pros:** Simple, fast, no setup, shareable
**Cons:** API calls from browser (but that's okay!)

### VS Code Extension

```
You install VS Code
    ↓
Install extension via marketplace
    ↓
Sidebar button appears
    ↓
Extension code runs in VS Code process
    ↓
Can access VS Code APIs and workspace
    ↓
More integrated experience
```

**Pros:** Integrated with code editor, powerful
**Cons:** More complex, requires build process

---

## ⚡ Right Now

### If You Don't Know What to Do:

1. Open `web/index.html` in your browser
2. Try it out
3. That's it!

### Next (Optional: Add AI)

1. Follow [`web/AI_SETUP_GUIDE.md`](web/AI_SETUP_GUIDE.md)
2. Pick one AI service (Google, OpenAI, or Claude)
3. Get your free/paid API key
4. Paste it in the app
5. Enjoy AI-powered task breakdown!

### Even Later (Optional: Share)

1. Deploy `web/` folder to GitHub Pages, Netlify, or Vercel
2. Share the URL
3. Others can use it!

---

## 💡 Current Status

✅ **Browser Version:** Complete and ready to use
✅ **VS Code Extension:** Complete and ready to use
✅ **AI Integrations:** Ready for all major services
✅ **Documentation:** Complete

---

## 🆘 Need Help?

**Browser version:** → Check [`web/README.md`](web/README.md)
**VS Code version:** → Check [`README.md`](README.md)
**AI setup:** → Check [`web/AI_SETUP_GUIDE.md`](web/AI_SETUP_GUIDE.md) or [`AI_INTEGRATION_EXAMPLES.md`](AI_INTEGRATION_EXAMPLES.md)
**Getting started:** → Check [`web/QUICK_START.md`](web/QUICK_START.md) or [`SETUP.md`](SETUP.md)

---

## 🎉 Let's Get Started!

**Pick one:**

### 👉 I want to start NOW (Browser)
Go to: **`web/QUICK_START.md`**

### 👉 I want VS Code integration
Go to: **`SETUP.md`**

### 👉 I want to understand first
Go to: **`web/README.md`**

---

**Ready?** Click one of the links above and let's go! 🚀
