import * as vscode from 'vscode';

let viewProvider: TaskDecomposerViewProvider;

export function activate(context: vscode.ExtensionContext) {
	console.log('Task Decomposer extension activated');

	viewProvider = new TaskDecomposerViewProvider(context.extensionUri, context);

	context.subscriptions.push(
		vscode.window.registerWebviewViewProvider(
			'taskDecomposerView',
			viewProvider
		)
	);

	context.subscriptions.push(
		vscode.commands.registerCommand('taskDecomposer.startTask', () => {
			viewProvider.startTask();
		})
	);

	context.subscriptions.push(
		vscode.commands.registerCommand('taskDecomposer.startComponent', (componentName: string) => {
			viewProvider.startComponent(componentName);
		})
	);
}

export function deactivate() {}

class TaskDecomposerViewProvider implements vscode.WebviewViewProvider {
	public static readonly viewType = 'taskDecomposerView';

	private _view?: vscode.WebviewView;
	private extensionUri: vscode.Uri;
	private context: vscode.ExtensionContext;
	private components: string[] = [];
	private currentComponentIndex: number = -1;
	private focusTimer: NodeJS.Timeout | null = null;
	private timerCount: number = 3;

	constructor(extensionUri: vscode.Uri, context: vscode.ExtensionContext) {
		this.extensionUri = extensionUri;
		this.context = context;
	}

	public resolveWebviewView(
		webviewView: vscode.WebviewView,
		context: vscode.WebviewViewResolveContext<any>,
		token: vscode.CancellationToken
	): void {
		this._view = webviewView;

		webviewView.webview.options = {
			enableScripts: true,
		};

		webviewView.webview.html = this.getHtmlContent();

		webviewView.webview.onDidReceiveMessage((data) => {
			this.handleWebviewMessage(data);
		});
	}

	private handleWebviewMessage(message: any): void {
		switch (message.command) {
			case 'askTask':
				void this.askForTask();
				break;
			case 'decomposeTask':
				void this.decomposeTask(message.task);
				break;
			case 'startComponent':
				this.startComponent(message.index);
				break;
		}
	}

	private async askForTask(): Promise<void> {
		const task = await vscode.window.showInputBox({
			placeHolder: 'Enter the task you want to break down...',
			prompt: 'What task would you like to decompose?'
		});

		if (task) {
			this._view?.webview.postMessage({ command: 'taskReceived', task: task });
			await this.decomposeTask(task);
		}
	}

	private async decomposeTask(task: string): Promise<void> {
		// Show progress
		this._view?.webview.postMessage({
			command: 'decomposing',
			message: 'Breaking down your task with AI...'
		});

		try {
			// TODO: Integrate with your AI API here
			// For now, we'll use a simple heuristic breakdown
			const components = await this.decomposeWithAI(task);

			this.components = components;
			this._view?.webview.postMessage({
				command: 'components',
				components: components
			});
		} catch (error) {
			vscode.window.showErrorMessage('Failed to decompose task: ' + String(error));
		}
	}

	private async decomposeWithAI(task: string): Promise<string[]> {
		// TODO: Replace this with actual AI API call
		// This is a placeholder implementation
		
		// Simple heuristic breakdown
		const commonSteps = [
			'Understand requirements',
			'Plan approach',
			'Implement solution',
			'Test and debug',
			'Review and optimize'
		];

		// For now, return generic steps
		// In production, call OpenAI, Claude, or your preferred AI service
		return commonSteps.map(step => `${step}: ${task}`);
	}

	public startTask(): void {
		const quickPick = vscode.window.createQuickPick<vscode.QuickPickItem>();
		quickPick.placeholder = 'Enter or paste your task...';
		quickPick.onDidChangeValue(() => {
			quickPick.items = [
				{
					label: quickPick.value,
					buttons: [
						{ iconPath: new vscode.ThemeIcon('play'), tooltip: 'Decompose' }
					]
				}
			];
		});
		quickPick.onDidTriggerItemButton(() => {
			void this.decomposeTask(quickPick.value);
			quickPick.hide();
		});
		quickPick.show();
	}

	public startComponent(componentNameOrIndex: string | number): void {
		let index: number;
		
		if (typeof componentNameOrIndex === 'string') {
			index = this.components.indexOf(componentNameOrIndex);
		} else {
			index = componentNameOrIndex;
		}

		if (index < 0 || index >= this.components.length) {
			vscode.window.showErrorMessage('Invalid component index');
			return;
		}

		this.currentComponentIndex = index;
		this.timerCount = 3;
		this.startFocusTimer();
	}

	private startFocusTimer(): void {
		// Send initial timer state
		this._view?.webview.postMessage({
			command: 'timerStart',
			component: this.components[this.currentComponentIndex],
			count: this.timerCount
		});

		// Update timer every second
		this.focusTimer = setInterval(() => {
			this.timerCount--;

			if (this.timerCount >= 0) {
				this._view?.webview.postMessage({
					command: 'timerTick',
					count: this.timerCount
				});
			} else {
				// Timer finished
				if (this.focusTimer) {
					clearInterval(this.focusTimer);
					this.focusTimer = null;
				}

				this._view?.webview.postMessage({
					command: 'timerComplete',
					component: this.components[this.currentComponentIndex]
				});

				vscode.window.showInformationMessage(
					`Focus time started for: ${this.components[this.currentComponentIndex]}`
				);
			}
		}, 1000);
	}

	private getHtmlContent(): string {
		return `<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Task Decomposer</title>
	<style>
		* {
			margin: 0;
			padding: 0;
			box-sizing: border-box;
		}

		body {
			font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
			padding: 12px;
			color: var(--vscode-foreground);
		}

		.container {
			width: 100%;
		}

		.section {
			margin-bottom: 16px;
		}

		h2 {
			font-size: 14px;
			font-weight: 600;
			margin-bottom: 8px;
			text-transform: uppercase;
			color: var(--vscode-foreground, #e0e0e0);
		}

		button {
			width: 100%;
			padding: 8px 12px;
			margin-bottom: 8px;
			background-color: var(--vscode-button-background);
			color: var(--vscode-button-foreground);
			border: none;
			border-radius: 2px;
			cursor: pointer;
			font-size: 13px;
			font-weight: 500;
		}

		button:hover {
			background-color: var(--vscode-button-hoverBackground);
		}

		.components-list {
			list-style: none;
		}

		.component-item {
			padding: 8px 12px;
			margin-bottom: 6px;
			background-color: var(--vscode-list-hoverBackground);
			border-radius: 3px;
			cursor: pointer;
			border-left: 3px solid transparent;
			display: flex;
			justify-content: space-between;
			align-items: center;
			transition: border-color 0.2s;
		}

		.component-item:hover {
			background-color: var(--vscode-list-activeSelectionBackground);
			border-left-color: var(--vscode-activityBarBadge-background);
		}

		.component-item.active {
			border-left-color: var(--vscode-focusBorder);
		}

		.component-text {
			font-size: 12px;
			flex: 1;
		}

		.component-button {
			padding: 4px 8px;
			font-size: 11px;
			min-width: 60px;
		}

		.timer-display {
			text-align: center;
			padding: 20px;
			background-color: var(--vscode-editor-background);
			border-radius: 4px;
			margin-bottom: 12px;
		}

		.timer-number {
			font-size: 48px;
			font-weight: bold;
			color: var(--vscode-textLink-foreground);
			margin-bottom: 8px;
		}

		.timer-label {
			font-size: 12px;
			color: var(--vscode-foreground);
		}

		.status-message {
			padding: 8px 12px;
			margin-bottom: 8px;
			background-color: var(--vscode-notifications-background);
			border-radius: 3px;
			font-size: 12px;
		}

		.status-message.info {
			border-left: 3px solid var(--vscode-statusBar-background);
		}

		.hidden {
			display: none;
		}
	</style>
</head>
<body>
	<div class="container">
		<div class="section">
			<h2>Task Decomposer</h2>
			<button id="startBtn">Start New Task</button>
		</div>

		<div id="taskSection" class="section hidden">
			<div id="statusMessage" class="status-message info"></div>
		</div>

		<div id="timerSection" class="section hidden">
			<div class="timer-display">
				<div class="timer-number" id="timerNumber">3</div>
				<div class="timer-label">Get ready to focus...</div>
			</div>
		</div>

		<div id="componentsSection" class="section hidden">
			<h2>Components</h2>
			<ul id="componentsList" class="components-list"></ul>
		</div>
	</div>

	<script>
		const vscode = acquireVsCodeApi();

		document.getElementById('startBtn').addEventListener('click', () => {
			vscode.postMessage({ command: 'askTask' });
		});

		window.addEventListener('message', (event) => {
			const message = event.data;

			switch (message.command) {
				case 'decomposing':
					showStatus(message.message);
					break;

				case 'components':
					displayComponents(message.components);
					break;

				case 'timerStart':
					showTimer(message.component, message.count);
					break;

				case 'timerTick':
					updateTimer(message.count);
					break;

				case 'timerComplete':
					completeTimer(message.component);
					break;
			}
		});

		function showStatus(message) {
			const taskSection = document.getElementById('taskSection');
			const statusMessage = document.getElementById('statusMessage');
			statusMessage.textContent = message;
			taskSection.classList.remove('hidden');
		}

		function displayComponents(components) {
			const componentsList = document.getElementById('componentsList');
			const componentsSection = document.getElementById('componentsSection');
			
			componentsList.innerHTML = '';

			components.forEach((component, index) => {
				const li = document.createElement('li');
				li.className = 'component-item';
				
				const textSpan = document.createElement('span');
				textSpan.className = 'component-text';
				textSpan.textContent = component;
				
				const btn = document.createElement('button');
				btn.className = 'component-button';
				btn.textContent = 'Start';
				btn.addEventListener('click', () => {
					vscode.postMessage({ command: 'startComponent', index: index });
				});

				li.appendChild(textSpan);
				li.appendChild(btn);
				componentsList.appendChild(li);
			});

			componentsSection.classList.remove('hidden');
		}

		function showTimer(component, count) {
			const timerSection = document.getElementById('timerSection');
			const timerNumber = document.getElementById('timerNumber');
			timerNumber.textContent = count;
			timerSection.classList.remove('hidden');
		}

		function updateTimer(count) {
			const timerNumber = document.getElementById('timerNumber');
			timerNumber.textContent = count;
		}

		function completeTimer(component) {
			const timerSection = document.getElementById('timerSection');
			timerSection.classList.add('hidden');
		}
	</script>
</body>
</html>`;
	}
}
