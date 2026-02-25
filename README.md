# Micro-Agent Framework

A minimal AI agent framework that runs entirely on local Ollama instances.

## Features

- **500 lines of code** (vs. 50,000+ in LangChain)
- **Runs on Ollama** (free, private, offline)
- **Full execution traces** (see exactly what the agent thought)
- **JSON-based ReAct** (structured reasoning and actions)
- **Safe math evaluation** (uses `simpleeval` instead of `eval`)
- **Real weather API** (WeatherAPI.com integration)
- **Environment configuration** (secure API key management)

## Quick Start

1. **Install Ollama**: https://ollama.ai
2. **Pull a model**: `ollama pull gemma3:4b`
3. **Install dependencies**: `pip install -r requirements.txt`
4. **Set up environment**: `cp .env.example .env` and add your API keys
5. **Run**: `python examples/basic_usage.py`

## Environment Variables

Create a `.env` file with:

```bash
# Weather API (get free key from https://www.weatherapi.com/my/)
WEATHERAPI_KEY=your_weatherapi_key_here

# Ollama configuration
LLM_BASE_URL=http://localhost:11434
LLM_MODEL=gemma3:4b
```

## Usage Examples

### Weather Query
```python
from engine import MicroAgent

agent = MicroAgent()
result = agent.run("What's the weather like in Karachi?")
print(result)
# Output: "The weather in Karachi is Mist, 74°F"
```

### Math Calculation
```python
agent = MicroAgent()
result = agent.run("Calculate (15 * 7) + 23")
print(result)
# Output: "128"
```

### Adding Your Own Tools

```python
from tools import tool

@tool
def my_custom_function(param1: str, param2: int):
    """Your tool description here"""
    return f"Processed: {param1} with {param2}"
```

## Architecture

- **ReAct Pattern**: Agent reasons about what to do, then acts
- **Tool Registry**: Decorator-based system for registering tools
- **JSON Communication**: Structured data exchange with LLM
- **Execution Tracing**: Complete decision history saved to JSON

## Why This Over Existing Solutions?

- **Simplicity**: 500 lines vs 50,000+ in frameworks like LangChain
- **Privacy**: Runs entirely on your machine, no data exfiltration
- **Transparency**: Full execution traces, see exactly what the agent "thought"
- **Performance**: No complex abstractions, direct tool execution
- **Local-First**: Works offline once models are downloaded

## File Structure

```
micro-agent/
├── src/
│   ├── llm_client.py    # Ollama communication
│   ├── tools.py         # Tool registry and implementations
│   └── engine.py        # ReAct reasoning loop
├── examples/
│   └── basic_usage.py  # Usage examples
├── .env.example          # Environment template
├── requirements.txt       # Dependencies
└── README.md           # This file
```

## Dependencies

- **Local-first**: Runs entirely on Ollama without external APIs
- **Tool Registry**: Simple decorator-based tool registration
- **Execution Tracing**: Complete decision history saved to JSON
- **ReAct Pattern**: Reasoning before acting for better decision making
- **Extensible**: Easy to add new tools via Python decorators

## License

MIT License - see LICENSE file for details.
