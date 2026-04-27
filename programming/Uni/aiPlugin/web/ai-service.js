/**
 * AI Service - Handles all AI API integrations
 * Supports: OpenAI, Anthropic Claude, Google Gemini, and placeholder mode
 */

const AIService = {
	/**
	 * Main decompose method - routes to appropriate AI service
	 */
	async decompose(task) {
		const apiType = Config.getApiType();
		const apiKey = Config.getApiKey();

		switch (apiType) {
			case 'openai':
				return this.decomposeWithOpenAI(task, apiKey);
			case 'anthropic':
				return this.decomposeWithAnthropic(task, apiKey);
			case 'google':
				return this.decomposeWithGoogle(task, apiKey);
			case 'none':
			default:
				return this.decomposeWithPlaceholder(task);
		}
	},

	/**
	 * OPTION 1: OpenAI (ChatGPT)
	 * Requires: API key from platform.openai.com/api-keys
	 */
	async decomposeWithOpenAI(task, apiKey) {
		const response = await fetch('https://api.openai.com/v1/chat/completions', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Bearer ${apiKey}`
			},
			body: JSON.stringify({
				model: 'gpt-3.5-turbo',
				messages: [
					{
						role: 'system',
						content: 'You are a task decomposition expert. Break down tasks into 3-5 specific, actionable steps. Always respond with valid JSON only.'
					},
					{
						role: 'user',
						content: `Break down this task into key components: "${task}"\n\nRespond with ONLY a JSON array of strings, like: ["Step 1: ...", "Step 2: ...", ...]`
					}
				],
				temperature: 0.7,
				max_tokens: 500
			})
		});

		if (!response.ok) {
			throw new Error(`OpenAI API error: ${response.statusText}`);
		}

		const data = await response.json();
		const content = data.choices[0].message.content;
		
		// Parse JSON from response
		const jsonMatch = content.match(/\[[\s\S]*\]/);
		if (!jsonMatch) {
			throw new Error('Invalid response format from OpenAI');
		}

		return JSON.parse(jsonMatch[0]);
	},

	/**
	 * OPTION 2: Anthropic Claude
	 * Requires: API key from console.anthropic.com
	 */
	async decomposeWithAnthropic(task, apiKey) {
		const response = await fetch('https://api.anthropic.com/v1/messages', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'x-api-key': apiKey,
				'anthropic-version': '2023-06-01'
			},
			body: JSON.stringify({
				model: 'claude-3-5-sonnet-20241022',
				max_tokens: 500,
				messages: [
					{
						role: 'user',
						content: `Break down this task into 3-5 specific, actionable steps. Always respond with ONLY valid JSON.\n\nTask: "${task}"\n\nRespond with ONLY a JSON array of strings, like: ["Step 1: ...", "Step 2: ...", ...]`
					}
				]
			})
		});

		if (!response.ok) {
			throw new Error(`Anthropic API error: ${response.statusText}`);
		}

		const data = await response.json();
		const content = data.content[0].text;

		// Parse JSON from response
		const jsonMatch = content.match(/\[[\s\S]*\]/);
		if (!jsonMatch) {
			throw new Error('Invalid response format from Anthropic');
		}

		return JSON.parse(jsonMatch[0]);
	},

	/**
	 * OPTION 3: Google Gemini
	 * Requires: API key from makersuite.google.com/app/apikey
	 */
	async decomposeWithGoogle(task, apiKey) {
		const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				contents: [{
					parts: [{
						text: `Break down this task into 3-5 specific, actionable steps. Always respond with ONLY valid JSON.\n\nTask: "${task}"\n\nRespond with ONLY a JSON array of strings, like: ["Step 1: ...", "Step 2: ...", ...]`
					}]
				}],
				generationConfig: {
					temperature: 0.7,
					maxOutputTokens: 500
				}
			})
		});

		if (!response.ok) {
			throw new Error(`Google API error: ${response.statusText}`);
		}

		const data = await response.json();
		const content = data.candidates[0].content.parts[0].text;

		// Parse JSON from response
		const jsonMatch = content.match(/\[[\s\S]*\]/);
		if (!jsonMatch) {
			throw new Error('Invalid response format from Google');
		}

		return JSON.parse(jsonMatch[0]);
	},

	/**
	 * PLACEHOLDER: Generic task breakdown (no API needed)
	 */
	async decomposeWithPlaceholder(task) {
		return new Promise((resolve) => {
			// Simulate processing delay
			setTimeout(() => {
				const steps = [
					'Understand requirements and scope',
					'Plan approach and break down steps',
					'Implement the solution',
					'Test and debug thoroughly',
					'Review, optimize, and finalize'
				];

				const components = steps.map(step => `${step}: ${task}`);
				resolve(components);
			}, 1500);
		});
	},

	/**
	 * Get setup instructions for each AI service
	 */
	getSetupInstructions(apiType) {
		const instructions = {
			openai: {
				title: 'OpenAI Setup',
				steps: [
					'1. Go to https://platform.openai.com/api-keys',
					'2. Create an account or sign in',
					'3. Click "Create new secret key"',
					'4. Copy the API key',
					'5. Paste it below'
				],
				link: 'https://platform.openai.com/api-keys',
				linkText: 'Get OpenAI API Key →'
			},
			anthropic: {
				title: 'Anthropic Claude Setup',
				steps: [
					'1. Go to https://console.anthropic.com/',
					'2. Create an account or sign in',
					'3. Go to API keys section',
					'4. Create a new API key',
					'5. Copy and paste it below'
				],
				link: 'https://console.anthropic.com/',
				linkText: 'Get Claude API Key →'
			},
			google: {
				title: 'Google Gemini Setup',
				steps: [
					'1. Go to https://makersuite.google.com/app/apikey',
					'2. Sign in with your Google account',
					'3. Click "Create API key"',
					'4. Copy the API key',
					'5. Paste it below'
				],
				link: 'https://makersuite.google.com/app/apikey',
				linkText: 'Get Gemini API Key →'
			}
		};

		return instructions[apiType] || null;
	}
};
