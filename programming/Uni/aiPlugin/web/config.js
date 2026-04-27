/**
 * Configuration and Storage Management
 */

const Config = {
	// Storage keys
	STORAGE_API_KEY: 'taskDecomposer_apiKey',
	STORAGE_API_TYPE: 'taskDecomposer_apiType',
	STORAGE_TASKS: 'taskDecomposer_tasks',

	// Get API key from localStorage
	getApiKey() {
		return localStorage.getItem(this.STORAGE_API_KEY) || null;
	},

	// Set API key in localStorage
	setApiKey(apiKey, apiType) {
		localStorage.setItem(this.STORAGE_API_KEY, apiKey);
		localStorage.setItem(this.STORAGE_API_TYPE, apiType);
	},

	// Get API type
	getApiType() {
		return localStorage.getItem(this.STORAGE_API_TYPE) || 'none';
	},

	// Clear API settings
	clearApiKey() {
		localStorage.removeItem(this.STORAGE_API_KEY);
		localStorage.removeItem(this.STORAGE_API_TYPE);
	},

	// Check if API is configured
	isApiConfigured() {
		return this.getApiKey() !== null;
	},

	// Save task history
	saveTask(task, components) {
		try {
			const tasks = JSON.parse(localStorage.getItem(this.STORAGE_TASKS) || '[]');
			tasks.unshift({
				id: Date.now(),
				task: task,
				components: components,
				createdAt: new Date().toISOString()
			});
			// Keep only last 20 tasks
			const limited = tasks.slice(0, 20);
			localStorage.setItem(this.STORAGE_TASKS, JSON.stringify(limited));
		} catch (error) {
			console.error('Failed to save task:', error);
		}
	},

	// Get task history
	getTaskHistory() {
		try {
			return JSON.parse(localStorage.getItem(this.STORAGE_TASKS) || '[]');
		} catch (error) {
			console.error('Failed to get task history:', error);
			return [];
		}
	}
};
