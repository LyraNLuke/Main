# Task Decomposer - Project Overview

## What You Built

A VS Code extension that:
1. Adds a button in the left sidebar
2. Opens a panel asking for a task
3. Uses AI to break it into components
4. Shows a timer before starting each component

## How It Works (Architecture)

```
User clicks icon in sidebar
    ↓
Sidebar panel opens (handled by VS Code)
    ↓
User enters task
    ↓
Extension sends to AI service
    ↓
AI returns list of components
    ↓
User clicks "Start" on a component
    ↓
Timer counts down (3, 2, 1, 0)
    ↓
Component work begins
```

## File Explanations

### `package.json`
- **What it is**: Configuration for your extension
- **Important parts**:
  - `activationEvents`: When the extension loads ("onView:taskDecomposerView" = when sidebar opens)
  - `contributes`: What your extension adds to VS Code
    - `viewsContainers`: The sidebar icon
    - `views`: The panel inside the sidebar
    - `commands`: Commands your extension can run
- **Edit when**: Adding new features or changing UI

### `tsconfig.json`
- **What it is**: TypeScript compiler settings
- **What it does**: Tells TypeScript how to convert .ts files to .js
- **Edit when**: Changing how strict type checking should be

### `src/extension.ts`
- **What it is**: The main code for your extension
- **What it does**:
  - Class `TaskDecomposerViewProvider`: Manages the sidebar panel
  - `resolveWebviewView()`: Creates the UI
  - `handleWebviewMessage()`: Listens for user interactions
  - `decomposeWithAI()`: **Placeholder** - replace this with real AI
  - `getHtmlContent()`: The webview UI code (HTML + CSS + JavaScript)

### `media/icon.svg`
- **What it is**: The small icon that appears in the sidebar
- **Edit when**: You want a different icon

### `README.md`
- **What it is**: User documentation
- **What it has**:
  - Feature list
  - Installation steps
  - AI integration options
  - Troubleshooting

### `SETUP.md`
- **What it is**: Getting started guide for you
- **What it has**: Step-by-step setup and common issues

### `AI_INTEGRATION_EXAMPLES.md`
- **What it is**: Copy-paste ready AI integration code
- **What it has**: 5 different AI services you can use

## Key Concepts

### WebviewView
- A panel that runs HTML/CSS/JavaScript inside VS Code
- Communication between VS Code code and webview uses `postMessage()`
- In `extension.ts`: VS Code side
- In `getHtmlContent()`: Webview side

### Message Flow

**VS Code → Webview** (sending data):
```typescript
this._view?.webview.postMessage({ command: 'components', components: [...] });
```

**Webview → VS Code** (sending data):
```javascript
vscode.postMessage({ command: 'askTask' });
```

**VS Code listens** to webview:
```typescript
webviewView.webview.onDidReceiveMessage((data) => { ... });
```

**Webview listens** to VS Code:
```javascript
window.addEventListener('message', (event) => { ... });
```

## Timer Mechanism

The timer works like this:

1. User clicks "Start" button on a component
2. `startComponent()` method in extension.ts runs
3. Timer is set to 3 seconds
4. Using `setInterval()`, count down every 1 second
5. Send countdown numbers to webview: 3, 2, 1, 0
6. Webview displays the number on screen
7. When reaches 0, show completion message

## AI Integration Hook

Currently the `decomposeWithAI()` method just returns generic steps:

```typescript
private async decomposeWithAI(task: string): Promise<string[]> {
    // This is a placeholder!
    const commonSteps = [...];
    return commonSteps;
}
```

You can replace this with real API calls. The method:
- Takes a task description (string)
- Calls an AI service
- Waits for response
- Returns array of component strings

## Building & Running

```
npm install          → Download dependencies
npm run esbuild      → Compile TypeScript to JavaScript
F5 (in VS Code)      → Launch extension in new window
Ctrl+Shift+R         → Reload in the new window
```

## Common Customizations

### Change Timer Duration
In `extension.ts`, find:
```typescript
private timerCount: number = 3;
```
Change `3` to any number (seconds)

### Change Icon
Replace `media/icon.svg` with your own SVG

### Change Panel Name
In `package.json`, find:
```json
"title": "Task Decomposer"
```
Change to whatever you want

### Change UI Layout
Edit the HTML in `getHtmlContent()` method
- It's a string with HTML inside
- And CSS styling inside `<style>` tags
- And JavaScript inside `<script>` tags

## Testing Tips

1. **Test the timer**: Click a component and watch the countdown
2. **Test messages**: Open DevTools (F12 in the extension window), go to Console
3. **Check errors**: Look in the "Output" panel → select "Task Decomposer" from dropdown
4. **Reload quickly**: Ctrl+Shift+R from the extension window

## Next: Add AI

Follow these steps:
1. Pick an AI service (OpenAI, Claude, etc.)
2. Get an API key
3. Open `AI_INTEGRATION_EXAMPLES.md`
4. Copy the code for your service
5. Paste into `src/extension.ts`
6. Replace `decomposeWithAI()` completely
7. Run `npm run esbuild`
8. F5 to test

## Package the Extension

When done, you can share it:

```powershell
npm install -g vsce
vsce package
```

This creates a `.vsix` file you can share.

## Resources

- **VS Code API**: https://code.visualstudio.com/api
- **Webview Guide**: https://code.visualstudio.com/api/extension-guides/webview
- **TypeScript**: https://www.typescriptlang.org/docs/
- **Examples**: https://github.com/microsoft/vscode-extension-samples

---

**Enjoy building!** 🚀
