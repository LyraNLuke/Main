/**
 * AI Integration Examples
 * 
 * This file shows various ways to integrate AI services into the Task Decomposer.
 * Copy the method that matches your chosen AI service and replace the decomposeWithAI method in extension.ts
 */

// ============================================================================
// OPTION 1: OpenAI (ChatGPT 3.5-turbo or GPT-4)
// ============================================================================
// npm install openai

export async function decomposeWithOpenAI(task: string): Promise<string[]> {
    const { OpenAI } = require('openai');

    const openai = new OpenAI({
        apiKey: process.env.OPENAI_API_KEY,
    });

    const message = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: [
            {
                role: "system",
                content: "You are a task decomposition expert. Break down tasks into 3-5 specific, actionable steps. Always respond with valid JSON only."
            },
            {
                role: "user",
                content: `Break down this task into key components: "${task}"\n\nRespond with ONLY a JSON array of strings, like: ["Step 1: ...", "Step 2: ...", ...]`
            }
        ],
        temperature: 0.7,
    });

    const content = message.choices[0].message.content;
    
    // Parse the JSON response
    const jsonMatch = content?.match(/\[[\s\S]*\]/);
    if (!jsonMatch) {
        throw new Error('Invalid response format from OpenAI');
    }
    
    const components: string[] = JSON.parse(jsonMatch[0]);
    return components;
}

// ============================================================================
// OPTION 2: Anthropic Claude
// ============================================================================
// npm install @anthropic-ai/sdk

export async function decomposeWithClaude(task: string): Promise<string[]> {
    const Anthropic = require("@anthropic-ai/sdk");

    const client = new Anthropic({
        apiKey: process.env.ANTHROPIC_API_KEY,
    });

    const message = await client.messages.create({
        model: "claude-3-5-sonnet-20241022",
        max_tokens: 1024,
        messages: [
            {
                role: "user",
                content: `Break down this task into 3-5 specific, actionable steps. Always respond with ONLY valid JSON.\n\nTask: "${task}"\n\nRespond with ONLY a JSON array of strings, like: ["Step 1: ...", "Step 2: ...", ...]`
            }
        ],
    });

    const content = message.content[0].type === 'text' ? message.content[0].text : '';
    
    // Parse the JSON response
    const jsonMatch = content.match(/\[[\s\S]*\]/);
    if (!jsonMatch) {
        throw new Error('Invalid response format from Claude');
    }
    
    const components: string[] = JSON.parse(jsonMatch[0]);
    return components;
}

// ============================================================================
// OPTION 3: Google Gemini
// ============================================================================
// npm install @google/generative-ai

export async function decomposeWithGemini(task: string): Promise<string[]> {
    const { GoogleGenerativeAI } = require("@google/generative-ai");

    const genAI = new GoogleGenerativeAI(process.env.GOOGLE_API_KEY);
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

    const prompt = `Break down this task into 3-5 specific, actionable steps. Always respond with ONLY valid JSON.\n\nTask: "${task}"\n\nRespond with ONLY a JSON array of strings, like: ["Step 1: ...", "Step 2: ...", ...]`;

    const result = await model.generateContent(prompt);
    const content = result.response.text();

    // Parse the JSON response
    const jsonMatch = content.match(/\[[\s\S]*\]/);
    if (!jsonMatch) {
        throw new Error('Invalid response format from Gemini');
    }

    const components: string[] = JSON.parse(jsonMatch[0]);
    return components;
}

// ============================================================================
// OPTION 4: Local/Custom API
// ============================================================================
// No npm install needed - uses fetch

export async function decomposeWithCustomAPI(task: string): Promise<string[]> {
    const response = await fetch('http://your-api-domain.com/api/decompose', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${process.env.CUSTOM_API_KEY}`
        },
        body: JSON.stringify({
            task: task,
            maxComponents: 5
        })
    });

    if (!response.ok) {
        throw new Error(`API error: ${response.statusText}`);
    }

    const data = await response.json();
    return data.components;
}

// ============================================================================
// OPTION 5: Ollama (Local LLM)
// ============================================================================
// No installation needed - uses fetch to local server
// Make sure Ollama is running: ollama serve

export async function decomposeWithOllama(task: string): Promise<string[]> {
    const response = await fetch('http://localhost:11434/api/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            model: 'mistral', // or 'llama2', 'neural-chat', etc.
            prompt: `Break down this task into 3-5 specific, actionable steps. Always respond with ONLY valid JSON.\n\nTask: "${task}"\n\nRespond with ONLY a JSON array of strings, like: ["Step 1: ...", "Step 2: ...", ...]`,
            stream: false,
        })
    });

    if (!response.ok) {
        throw new Error(`Ollama error: ${response.statusText}`);
    }

    const data = await response.json();
    const content = data.response;

    // Parse the JSON response
    const jsonMatch = content.match(/\[[\s\S]*\]/);
    if (!jsonMatch) {
        throw new Error('Invalid response format from Ollama');
    }

    const components: string[] = JSON.parse(jsonMatch[0]);
    return components;
}

// ============================================================================
// INTEGRATION INSTRUCTIONS
// ============================================================================
/*

1. Choose ONE of the options above based on your preference

2. For OpenAI:
   - Get API key: https://platform.openai.com/api-keys
   - Set: $env:OPENAI_API_KEY = "sk-..."
   - npm install openai
   - Use decomposeWithOpenAI

3. For Claude:
   - Get API key: https://console.anthropic.com/
   - Set: $env:ANTHROPIC_API_KEY = "sk-ant-..."
   - npm install @anthropic-ai/sdk
   - Use decomposeWithClaude

4. For Gemini:
   - Get API key: https://makersuite.google.com/app/apikey
   - Set: $env:GOOGLE_API_KEY = "..."
   - npm install @google/generative-ai
   - Use decomposeWithGemini

5. For Local Ollama:
   - Download: https://ollama.ai/
   - Run: ollama serve
   - Pull a model: ollama pull mistral
   - Use decomposeWithOllama

6. For Custom API:
   - Replace 'http://your-api-domain.com/api/decompose' with your endpoint
   - Use decomposeWithCustomAPI

After choosing:

1. Copy the function from above
2. Open src/extension.ts
3. Replace the decomposeWithAI method with your chosen function
4. Run: npm run esbuild
5. Press F5 to test

*/
