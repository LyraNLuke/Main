# 📖 Documentation Index

Welcome to the AI Task Breakdown Browser Extension! Here's a guide to all the documentation files.

## 🚀 **Start Here!**

### [GETTING_STARTED.md](./GETTING_STARTED.md) ← **Read This First!**
A step-by-step checklist to get everything set up and running in about 15 minutes.
- System setup
- Building the extension
- Loading into Chrome
- Testing with Ollama
- Troubleshooting by OS

**Time:** 15 minutes | **Skill Level:** Beginner

---

## 📚 Complete Documentation

### [README.md](./README.md)
The main documentation file with:
- Feature overview
- Installation instructions
- Usage guide
- Development setup
- How to modify AI backends
- Privacy & storage info
- Known limitations & future features

**Time:** 10-15 minutes | **Skill Level:** Intermediate

### [QUICKSTART.md](./QUICKSTART.md)
A condensed 5-minute version if you're in a hurry:
- Install Ollama (1 min)
- Build extension (2 min)
- Load in Chrome (1 min)
- Start using (1 min)
- Quick troubleshooting

**Time:** 5 minutes | **Skill Level:** Beginner

### [PROJECT_OVERVIEW.md](./PROJECT_OVERVIEW.md)
Deep dive into how everything works:
- User flow diagram
- Architecture overview (with ASCII diagrams!)
- Complete file structure
- Data flow explained
- Technology stack
- How AI breakdown works
- Storage structure
- Extension lifecycle
- Common questions & answers

**Time:** 15-20 minutes | **Skill Level:** Intermediate/Advanced

### [SETUP.md](./SETUP.md)
Advanced setup and configuration guide:
- Detailed system requirements
- Step-by-step installation for Windows/Mac/Linux
- Ollama installation and verification
- Build troubleshooting
- Performance optimization
- Development workflow
- Custom configuration
- Alternative AI providers
- Deployment considerations

**Time:** 20-30 minutes | **Skill Level:** Advanced

---

## 📋 Decision Guide: Which File Should I Read?

### "I just want to get it working NOW!"
→ Read: **GETTING_STARTED.md** (then QUICKSTART.md if you want)

### "I want to understand what this does"
→ Read: **README.md** or **PROJECT_OVERVIEW.md**

### "I need more details on setup/troubleshooting"
→ Read: **SETUP.md** (organized by OS)

### "I want to understand the code/architecture"
→ Read: **PROJECT_OVERVIEW.md** then dive into source files

### "I'm having a specific problem"
→ Read: **SETUP.md** troubleshooting section OR **GETTING_STARTED.md** common issues

### "I want to modify/extend the extension"
→ Read: **PROJECT_OVERVIEW.md** then **README.md** development section

---

## 🗂️ File Structure

```
extension/                              # Main extension folder
├── src/                                # Source code (TypeScript/React)
│   ├── popup/                          # Browser popup UI
│   ├── background/                     # Background service worker
│   ├── content/                        # Injected content script
│   ├── utils/                          # Utility functions
│   └── types/                          # TypeScript type definitions
│
├── public/                             # Public assets
│   ├── popup.html                      # Extension popup HTML
│   └── styles/                         # Global styles
│
├── dist/                               # Compiled output (created by npm run build)
│
├── Documentation
│   ├── README.md                       # Main docs
│   ├── QUICKSTART.md                   # 5-min quick start
│   ├── GETTING_STARTED.md              # ← Start here! (checklist)
│   ├── SETUP.md                        # Advanced setup guide
│   ├── PROJECT_OVERVIEW.md             # Architecture & flow
│   └── INDEX.md                        # This file!
│
├── manifest.json                       # Extension configuration
├── package.json                        # Dependencies
├── tsconfig.json                       # TypeScript config
└── webpack.config.js                   # Build configuration
```

---

## ⚡ Quick Command Reference

```bash
# Installation
npm install                  # Install dependencies
npm run build               # Build for production
npm run dev                 # Build in watch mode (auto-rebuild)

# Extension location
chrome://extensions/        # Load/manage extensions

# Ollama setup
ollama pull llama2          # Download LLM model
ollama list                 # See installed models

# Verification
node --version              # Check Node.js
npm --version               # Check npm
curl http://localhost:11434 # Check Ollama running
```

---

## 🎯 Key Features at a Glance

```
┌─────────────────────────────────────────┐
│     AI TASK BREAKDOWN ASSISTANT         │
├─────────────────────────────────────────┤
│ ✨ AI-powered task decomposition        │
│ ⏱️  5-second countdown timer             │
│ ⏱️  Stopwatch time tracking              │
│ 💾 Local browser storage                │
│ 🎯 Progress tracking                   │
│ 📌 Floating draggable widget            │
│ 🎨 Beautiful modern UI                  │
│ 🔒 Complete privacy (offline)           │
└─────────────────────────────────────────┘
```

---

## 🔧 Technology Stack

- **Frontend:** React 18 + TypeScript
- **Extension:** Chrome Manifest V3
- **Build:** Webpack + Babel
- **AI:** Ollama (local LLM - free!)
- **Storage:** Chrome Storage API
- **Styling:** CSS3 with gradients & animations

---

## 📞 Need Help?

1. **For setup:** Check [GETTING_STARTED.md](./GETTING_STARTED.md) → TROUBLESHOOTING section
2. **For issues:** See [SETUP.md](./SETUP.md) → TROUBLESHOOTING section
3. **For how it works:** Read [PROJECT_OVERVIEW.md](./PROJECT_OVERVIEW.md)
4. **For features:** Check [README.md](./README.md)

---

## 🎉 Ready to Start?

**[➡️ Go to GETTING_STARTED.md](./GETTING_STARTED.md)**

Or if you're experienced:
- [Quick Setup (5 min)](./QUICKSTART.md)
- [Full Docs](./README.md)

---

**Version:** 1.0.0  
**Last Updated:** 2026-04-28  
**Status:** Ready to build! 🚀
