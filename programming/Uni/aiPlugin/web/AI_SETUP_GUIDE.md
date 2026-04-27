# Task Decomposer - Browser AI Integration Guide

This guide explains how to set up each AI service for the browser version. Choose one and follow the steps.

## 🎯 Overview

The browser version has 4 AI integration options built-in:

| Service | Setup Time | Quality | Cost | Free Tier |
|---------|-----------|---------|------|-----------|
| **Placeholder** | 0 min | Basic | FREE | Yes |
| **Google Gemini** | 5 min | Good | $0.0001/task | Yes |
| **OpenAI (GPT)** | 5 min | Excellent | $0.001/task | No |
| **Anthropic Claude** | 5 min | Excellent | $0.002/task | No |

## Option 1: Skip Setup (Placeholder) ✅ EASIEST

**When to use:** You want to try the app immediately, don't need AI

**How:**
1. Open `index.html`
2. Click "Get Started"
3. Click "Skip for Now"
4. Use generic task breakdown
5. Works completely offline

**Cost:** FREE
**Quality:** Basic (generic steps)
**Time:** 0 minutes

---

## Option 2: Google Gemini ✅ RECOMMENDED FOR FREE

**When to use:** You want free AI with decent quality

**Setup (5 minutes):**

### Step 1: Create API Key
1. Go to https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Choose "Create API Key in new project"
4. Copy the API key

### Step 2: Add to App
1. Open `index.html` in browser
2. Click "Get Started"
3. Select "Google Gemini" card
4. Paste API key
5. Click "Save API Key"

### Step 3: Use It
1. Enter a task
2. Click "Decompose Task"
3. Enjoy AI-powered breakdown!

**Cost:** Free tier (~$300/month), then pay-as-you-go
**Quality:** Good
**Speed:** Fast
**Supported:** Multimodal

**Troubleshooting:**
- "API error 403": Free tier limit exceeded, switch to paid or use different service
- "API error 400": API key invalid, get a new one

---

## Option 3: OpenAI (ChatGPT) ⭐ BEST QUALITY

**When to use:** You want the best AI quality, don't mind paying

**Setup (5 minutes):**

### Step 1: Create API Key
1. Go to https://platform.openai.com/api-keys
2. Sign up or sign in
3. Click "Create new secret key"
4. Copy it immediately (you won't see it again!)

### Step 2: Add Credits (Optional but recommended)
1. In same account, go to Billing
2. Add payment method
3. Set usage limits if desired

### Step 3: Add to App
1. Open `index.html` in browser
2. Click "Get Started"
3. Select "OpenAI" card
4. Paste API key
5. Click "Save API Key"

### Step 4: Use It
1. Enter a task
2. Click "Decompose Task"
3. Get excellent AI breakdown!

**Cost:** $0.0005-0.001 per task (~$0.02-0.04 per 50 tasks)
**Quality:** Excellent (GPT-3.5)
**Speed:** Very fast
**Supported:** Text only

**Example Costs:**
- 100 tasks = ~$0.05-1.00
- 1000 tasks = ~$0.50-1.00

**Troubleshooting:**
- "API key invalid": Check you copied entire key without spaces
- "Quota exceeded": Add payment method or credits
- "API error": Check internet connection

**Monitor Usage:**
1. Go to https://platform.openai.com/account/billing/overview
2. Check current usage
3. Set spending limit if needed

---

## Option 4: Anthropic Claude

**When to use:** You want excellent quality, prefer Claude's reasoning

**Setup (5 minutes):**

### Step 1: Create API Key
1. Go to https://console.anthropic.com
2. Sign up or sign in
3. Click API keys
4. Create new API key
5. Copy it

### Step 2: Add Credits
1. Go to Billing in same account
2. Add payment method

### Step 3: Add to App
1. Open `index.html` in browser
2. Click "Get Started"
3. Select "Anthropic Claude" card
4. Paste API key
5. Click "Save API Key"

### Step 4: Use It
1. Enter a task
2. Click "Decompose Task"
3. See Claude's breakdown!

**Cost:** $0.001-0.002 per task
**Quality:** Excellent (better reasoning than GPT)
**Speed:** Slightly slower than OpenAI
**Supported:** Text only

**Troubleshooting:**
- "API error": Check key is valid
- "Quota exceeded": Add payment method

---

## How to Change Your Choice Later

### Switch to Different AI Service

1. Open browser console (F12)
2. Run: `localStorage.clear()`
3. Refresh browser
4. Start over with new service

Or manually:
```javascript
// In browser console (F12):
localStorage.removeItem('taskDecomposer_apiKey');
localStorage.removeItem('taskDecomposer_apiType');
location.reload();
```

---

## Comparison Table

| Feature | Gemini (Free) | OpenAI | Claude | Placeholder |
|---------|---------------|--------|--------|-------------|
| Cost | Free | $0.001/task | $0.002/task | Free |
| Quality | Good | Excellent | Excellent | Basic |
| Setup | 5 min | 5 min | 5 min | 0 min |
| Speed | Fast | Very Fast | Good | N/A |
| Free Tier | Yes | No | No | Yes |
| Requires Payment | No | Yes | Yes | No |
| Works Offline | No | No | No | Yes |

---

## FAQ

### Q: Where is my API key stored?
**A:** In browser's localStorage, nowhere else. Your key never leaves your browser except to call the AI service.

### Q: Can I use multiple AI services?
**A:** Only one at a time. You can switch in browser console (see above).

### Q: Is it safe?
**A:** Yes for personal use. Not recommended for shared computers. Clear localStorage before closing if shared.

### Q: How much will it cost?
**A:** 
- Google Gemini: Free + potential costs
- OpenAI: ~$0.001 per task (~$1 for 1000 tasks)
- Claude: ~$0.002 per task (~$2 for 1000 tasks)
- Placeholder: FREE

### Q: My API key isn't working
**A:**
1. Copy key again carefully (no extra spaces)
2. Check it's the right service
3. Verify API key is active and not revoked
4. Ensure you have credits remaining (if paid service)

### Q: Can I use my own backend AI?
**A:** Yes! Edit `ai-service.js` and add your own API call. Backend should:
- Accept POST with `task` parameter
- Return `{ "components": ["step 1", "step 2", ...] }`
- Handle CORS headers

### Q: Which should I choose?
**A:** Start with Google Gemini (free), if it hits limits switch to OpenAI (best quality/price ratio).

---

## Next Steps

1. **Try without AI:** Skip setup, use placeholder
2. **Get free AI:** Setup Google Gemini
3. **Want best quality:** Setup OpenAI
4. **Already using Claude:** Setup Anthropic

Pick one and follow the steps above!

Need help? Check [README.md](README.md) or [QUICK_START.md](QUICK_START.md).

---

**Ready?** Start with Option 2 (Google Gemini - Free) 🚀
