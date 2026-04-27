/**
 * Task Decomposer - Main Application Logic
 */

class TaskDecomposerApp {
	constructor() {
		this.currentTask = '';
		this.currentComponents = [];
		this.currentComponentIndex = -1;
		this.timerCount = 3;
		this.timerInterval = null;
		this.selectedApiType = null;

		this.initializeEventListeners();
		this.checkApiConfiguration();
	}

	initializeEventListeners() {
		// Welcome screen
		document.getElementById('getStartedBtn')?.addEventListener('click', () => this.navigateTo('apiSetup'));

		// Sidebar
		document.getElementById('startTaskBtn')?.addEventListener('click', () => this.startNewTask());
		document.getElementById('settingsBtn')?.addEventListener('click', () => this.showSettings());

		// Widget open/close
		document.getElementById('pluginLauncher')?.addEventListener('click', () => this.openWidget());
		document.getElementById('closeWidgetBtn')?.addEventListener('click', () => this.closeWidget());
		document.getElementById('pluginOverlay')?.addEventListener('click', (event) => {
			if (event.target === document.getElementById('pluginOverlay')) {
				this.closeWidget();
			}
		});
		this.makeDraggable();

		// API Setup
		document.querySelectorAll('.api-card').forEach(card => {
			card.querySelector('.btn').addEventListener('click', () => {
				const apiType = card.dataset.api;
				if (apiType === 'none') {
					Config.clearApiKey();
					this.navigateTo('taskInput');
				} else {
					this.showApiKeyForm(apiType);
				}
			});
		});

		document.getElementById('backBtn')?.addEventListener('click', () => this.navigateTo('apiSetup'));
		document.getElementById('settingsBackBtn')?.addEventListener('click', () => this.navigateTo(this.currentTask ? 'components' : 'taskInput'));

		// Task Input
		document.getElementById('decomposeBtn')?.addEventListener('click', () => this.decomposeTask());
		document.getElementById('cancelTaskBtn')?.addEventListener('click', () => this.navigateTo('components'));
		document.getElementById('startNewTaskBtn')?.addEventListener('click', () => this.startNewTask());

		// Components
		document.getElementById('taskInput')?.addEventListener('keypress', (e) => {
			if (e.key === 'Enter' && e.ctrlKey) {
				this.decomposeTask();
			}
		});

		// Timer
		document.getElementById('skipTimerBtn')?.addEventListener('click', () => this.skipTimer());
		document.getElementById('acknowledgeTimerBtn')?.addEventListener('click', () => this.acknowledgeTimer());

		// Error
		document.getElementById('errorRetryBtn')?.addEventListener('click', () => this.navigateTo('taskInput'));
	}

	checkApiConfiguration() {
		if (Config.isApiConfigured()) {
			this.navigateTo('taskInput');
		} else {
			this.navigateTo('welcome');
		}
	}

	navigateTo(screenId) {
		// Hide all screens
		document.querySelectorAll('.screen').forEach(screen => {
			screen.classList.remove('active');
		});

		// Show target screen
		const targetScreen = document.getElementById(screenId + 'Screen');
		if (targetScreen) {
			targetScreen.classList.add('active');
		}
	}

	startNewTask() {
		document.getElementById('taskInput').value = '';
		document.getElementById('decomposingStatus').classList.add('hidden');
		this.navigateTo('taskInput');
	}

	async decomposeTask() {
		const task = document.getElementById('taskInput').value.trim();

		if (!task) {
			this.showError('Task Required', 'Please enter a task to decompose.');
			return;
		}

		this.currentTask = task;

		// Show decomposing status
		document.getElementById('decomposingStatus').classList.remove('hidden');

		try {
			const components = await AIService.decompose(task);

			if (!Array.isArray(components) || components.length === 0) {
				throw new Error('No components returned from AI');
			}

			this.currentComponents = components;
			Config.saveTask(task, components);
			this.displayComponents();
			this.navigateTo('components');

		} catch (error) {
			console.error('Decomposition error:', error);
			this.showError('Decomposition Failed', error.message || 'Failed to decompose task. Please check your API key or try again.');
			document.getElementById('decomposingStatus').classList.add('hidden');
		}
	}

	displayComponents() {
		const componentsList = document.getElementById('componentsList');
		const noComponents = document.getElementById('noComponents');
		const taskTitle = document.getElementById('taskTitle');

		taskTitle.textContent = this.currentTask;
		componentsList.innerHTML = '';

		if (this.currentComponents.length === 0) {
			noComponents.classList.remove('hidden');
			return;
		}

		noComponents.classList.add('hidden');

		this.currentComponents.forEach((component, index) => {
			const item = document.createElement('div');
			item.className = 'component-item';
			item.innerHTML = `
				<div class="component-number">${index + 1}</div>
				<div class="component-text">${this.escapeHtml(component)}</div>
				<button class="btn btn-primary" data-index="${index}">Start</button>
			`;

			item.querySelector('.btn').addEventListener('click', () => {
				this.startComponent(index);
			});

			componentsList.appendChild(item);
		});
	}

	startComponent(index) {
		if (index < 0 || index >= this.currentComponents.length) {
			this.showError('Invalid Component', 'Component not found.');
			return;
		}

		this.currentComponentIndex = index;
		this.timerCount = 3;
		this.showTimer();
		this.navigateTo('timer');
	}

	showTimer() {
		const componentName = this.currentComponents[this.currentComponentIndex];
		document.getElementById('timerComponentName').textContent = componentName;
		document.getElementById('timerNumber').textContent = this.timerCount;
		document.getElementById('timerFinished').classList.add('hidden');
		document.getElementById('skipTimerBtn').style.display = 'block';

		// Clear any existing timer
		if (this.timerInterval) {
			clearInterval(this.timerInterval);
		}

		// Start countdown
		this.timerInterval = setInterval(() => {
			this.timerCount--;
			document.getElementById('timerNumber').textContent = Math.max(0, this.timerCount);

			if (this.timerCount < 0) {
				clearInterval(this.timerInterval);
				this.completeTimer();
			}
		}, 1000);
	}

	completeTimer() {
		document.getElementById('skipTimerBtn').style.display = 'none';
		document.getElementById('timerFinished').classList.remove('hidden');
	}

	skipTimer() {
		if (this.timerInterval) {
			clearInterval(this.timerInterval);
		}
		this.completeTimer();
	}

	acknowledgeTimer() {
		// Mark component as in progress
		const componentItems = document.querySelectorAll('.component-item');
		if (componentItems[this.currentComponentIndex]) {
			componentItems[this.currentComponentIndex].classList.add('completed');
		}

		// Show next component or go back to list
		if (this.currentComponentIndex + 1 < this.currentComponents.length) {
			this.startComponent(this.currentComponentIndex + 1);
		} else {
			this.navigateTo('components');
		}
	}

	showApiKeyForm(apiType) {
		const form = document.getElementById('apiKeyForm');
		const instructions = AIService.getSetupInstructions(apiType);

		if (!instructions) {
			this.showError('Invalid API Type', 'Unknown API type selected.');
			return;
		}

		form.innerHTML = `
			<h3>${instructions.title}</h3>
			<div style="text-align: left; margin-bottom: 20px;">
				${instructions.steps.map(step => `<div style="margin-bottom: 8px; font-size: 13px;">${step}</div>`).join('')}
				${instructions.link ? `<div style="margin-top: 12px;"><a href="${instructions.link}" target="_blank" style="color: var(--color-primary); text-decoration: none;">${instructions.linkText}</a></div>` : ''}
			</div>
			<div class="form-group">
				<label for="apiKeyInput">API Key</label>
				<input type="password" id="apiKeyInput" placeholder="Paste your API key here..." />
				<div class="form-help">Your API key is only stored locally in your browser.</div>
			</div>
			<button class="btn btn-primary" id="saveApiKeyBtn">Save API Key</button>
		`;

		document.getElementById('saveApiKeyBtn').addEventListener('click', () => {
			const apiKey = document.getElementById('apiKeyInput').value.trim();

			if (!apiKey) {
				this.showError('API Key Required', 'Please enter your API key.');
				return;
			}

			Config.setApiKey(apiKey, apiType);
			this.navigateTo('taskInput');
		});

		this.navigateTo('apiKey');
	}

	openWidget() {
		const overlay = document.getElementById('pluginOverlay');
		const launcher = document.getElementById('pluginLauncher');
		if (!overlay) return;
		overlay.classList.add('active');
		launcher?.classList.add('hidden');

		const activeScreen = document.querySelector('.screen.active');
		if (!activeScreen) {
			this.navigateTo(Config.isApiConfigured() ? 'taskInput' : 'welcome');
		}
	}

	closeWidget() {
		const overlay = document.getElementById('pluginOverlay');
		const launcher = document.getElementById('pluginLauncher');
		if (!overlay) return;
		overlay.classList.remove('active');
		launcher?.classList.remove('hidden');
	}

	showSettings() {
		const content = document.getElementById('settingsContent');
		const apiType = Config.getApiType();
		const apiKey = Config.getApiKey();
		const displayService = apiType === 'none' ? 'None (placeholder)' : apiType.charAt(0).toUpperCase() + apiType.slice(1);
		const maskedKey = apiKey ? `${apiKey.slice(0, 4)}••••••••${apiKey.slice(-4)}` : '<em>Not configured</em>';

		content.innerHTML = `
			<h3>Settings</h3>
			<div class="form-group" style="margin-bottom: 20px; text-align: left;">
				<label>Current AI Configuration</label>
				<div style="padding: 14px; border: 1px solid var(--color-border); border-radius: 8px; background: var(--color-bg);">
					<div><strong>Service:</strong> ${displayService}</div>
					<div style="margin-top: 8px;"><strong>API Key:</strong> ${maskedKey}</div>
				</div>
			</div>
			<div class="task-input-actions" style="justify-content: flex-start; gap: 12px; flex-wrap: wrap;">
				<button class="btn btn-primary" id="changeApiBtn">Change API Key</button>
				<button class="btn btn-secondary" id="clearApiBtn">Clear API Key</button>
				<button class="btn btn-secondary" id="reconfigureApiBtn">Choose API Service</button>
			</div>
			<div class="form-help" style="margin-top: 16px; color: var(--color-text-secondary);">
				If you want to use built-in AI again, choose a service after clearing the key.
			</div>
		`;

		document.getElementById('changeApiBtn').addEventListener('click', () => {
			if (!apiKey || apiType === 'none') {
				this.navigateTo('apiSetup');
			} else {
				this.showApiKeyForm(apiType);
			}
		});

		document.getElementById('clearApiBtn').addEventListener('click', () => {
			Config.clearApiKey();
			this.showSettings();
		});

		document.getElementById('reconfigureApiBtn').addEventListener('click', () => {
			this.navigateTo('apiSetup');
		});

		this.navigateTo('settings');
	}

	showError(title, message) {
		document.getElementById('errorTitle').textContent = title;
		document.getElementById('errorMessage').textContent = message;
		this.navigateTo('error');
	}

	escapeHtml(text) {
		const div = document.createElement('div');
		div.textContent = text;
		return div.innerHTML;
	}
}

function initializeTaskDecomposer() {
	if (!window.app) {
		window.app = new TaskDecomposerApp();
	}
}

if (document.readyState === 'loading') {
	document.addEventListener('DOMContentLoaded', initializeTaskDecomposer);
} else {
	initializeTaskDecomposer();
}
