# Browser Version - Test It Right Now!

Your Task Decomposer browser version is **ready to use in 30 seconds**. Choose your method:

## Quick Test Options

### Option 1: Direct Open (Easiest!) ⭐
```
1. Open Windows File Explorer
2. Navigate to: C:\Users\Brian Geisler\OneDrive\programming\Uni\aiPlugin\web
3. Double-click: index.html
4. Done! App opens in default browser
```

✅ Works immediately
✅ No server setup
✅ No commands needed
❌ Some features may be limited in local file mode

### Option 2: Python Simple Server (Recommended)

```powershell
# 1. Open PowerShell in the web folder
cd "c:\Users\Brian Geisler\OneDrive\programming\Uni\aiPlugin\web"

# 2. Start server
python -m http.server 8000

# 3. Open in browser
start http://localhost:8000

# 4. To stop: Press Ctrl+C
```

✅ Full features enabled
✅ CORS works correctly
✅ All JavaScript features work
✅ Can access from other devices

**If Python not installed:**
- Download Python from python.org
- Run installer
- Check "Add Python to PATH"
- Restart PowerShell
- Try command again

### Option 3: Node.js http-server (If installed)

```powershell
cd "c:\Users\Brian Geisler\OneDrive\programming\Uni\aiPlugin\web"
npx http-server
# Then go to http://localhost:8080
```

### Option 4: PHP (If installed)

```powershell
cd "c:\Users\Brian Geisler\OneDrive\programming\Uni\aiPlugin\web"
php -S localhost:8000
# Then go to http://localhost:8000
```

---

## First Time Using

### What You'll See

1. **Welcome Screen**
   - Image of features
   - "Get Started" button
   - Shows: AI, Timer, Components

2. **Setup Screen** (click "Get Started")
   - 4 AI options shown as cards
   - OpenAI, Claude, Gemini, Skip options
   - Click one to proceed

3. **For Now: Click "Skip for Now"**
   - No AI setup needed
   - Uses placeholder breakdown
   - Good for testing

4. **Task Input** (where you enter task)
   - Text area for task description
   - "Decompose Task" button
   - Example: "Build a website"

5. **Components Display**
   - Shows 5 generic steps
   - Each has a "Start" button
   - Click "Start" to test timer

6. **Timer Screen**
   - Big number counting down from 3
   - "Get ready to focus..." text
   - When hits 0: Shows ✓ checkmark
   - Click "Start Working"

### Test Flow

```
1. Open index.html
2. Click "Get Started"
3. Click "Skip for Now"
4. Enter: "Build a mobile app"
5. Click "Decompose Task"
6. See generic components
7. Click "Start" on first component
8. Watch 3-second timer
9. See "Ready to focus!" message
10. Click "Start Working"
11. Back to component list
```

---

## First Time With AI (Optional)

Only if you want real AI breakdown:

### 1. Get Free API Key (2 minutes)
- Go: https://makersuite.google.com/app/apikey
- Click "Create API Key"
- Click "Create API Key in new project"
- Copy key

### 2. Setup in App
1. Open app in browser
2. Click "Get Started"
3. Click "Google Gemini"
4. Paste API key
5. Click "Save API Key"

### 3. Use AI
1. Enter: "Learn JavaScript"
2. Click "Decompose Task"
3. Wait a moment...
4. See AI-generated components!
5. Click "Start" on any component
6. Watch timer
7. Ready to focus!

---

## What to Test

### Test 1: Basic Flow
- [x] Open app
- [x] Click "Get Started"
- [x] Click "Skip for Now"
- [x] Enter a task
- [x] See components
- [x] Start timer
- [x] See countdown
- [x] See "Ready" message

### Test 2: Navigation
- [x] "New Task" button works
- [x] Can go back to components from timer
- [x] Can enter new task

### Test 3: Timer
- [x] Counts from 3 to 0
- [x] Takes 3 seconds
- [x] Shows "Get ready to focus..." text
- [x] Shows "Ready to focus!" after

### Test 4: UI
- [x] Dark theme looks good
- [x] Buttons are clickable
- [x] Text is readable
- [x] Icons show correctly
- [x] Colors match design

---

## Common Issues & Quick Fixes

### "Can't open index.html"
→ Use PowerShell method instead (Option 2)

### "Nothing shows up"
→ Refresh browser (Ctrl+R or Cmd+R)

### "Buttons don't work"
→ Open browser console (F12) and check for errors

### "Timer doesn't count"
→ Clear browser cache (Ctrl+Shift+Delete)

### "API setup not showing"
→ Clear localStorage: `localStorage.clear()` in F12 console

### "CORS error"
→ Use http:// not file:// (use Option 2: Python server)

---

## Keyboard Shortcuts

While in app:
- **F12** = Open Developer Tools (for debugging)
- **Ctrl+R** = Refresh page
- **Ctrl+Shift+Delete** = Clear browser storage

---

## Browser Compatibility

| Browser | Status | Version |
|---------|--------|---------|
| Chrome | ✅ Works | All |
| Firefox | ✅ Works | All |
| Safari | ✅ Works | All |
| Edge | ✅ Works | All |
| IE | ❌ Doesn't work | - |

Use Chrome, Firefox, Safari, or Edge for best experience.

---

## Next Steps

1. ✅ **Right now:** Test with Option 1 or 2 above
2. ⏭️ **After testing:** Read [`QUICK_START.md`](QUICK_START.md)
3. 🤖 **For AI:** Follow [`AI_SETUP_GUIDE.md`](AI_SETUP_GUIDE.md)
4. 📚 **For details:** Read [`README.md`](README.md)

---

## Ask Yourself

- [ ] Can I open the app? → Good!
- [ ] Can I click buttons? → Good!
- [ ] Does timer count down? → Good!
- [ ] Can I go back and forth? → Good!
- [ ] Want to try with real AI? → Do AI_SETUP_GUIDE.md

---

## You're Ready!

This is a complete, working web app. Everything works. Just:

1. Open index.html
2. Click buttons
3. Use it!

Enjoy! 🎉

---

**Questions?** Check README.md or AI_SETUP_GUIDE.md

**Ready to deploy?** See README.md "Deployment Options" section
