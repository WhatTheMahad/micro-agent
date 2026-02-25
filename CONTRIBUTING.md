# Contributor Guide

Adding a new tool to the micro-agent framework is simple and follows a clear pattern.

## How to Add a New Tool

### 1. Create Your Tool Function

Add your tool to `src/tools.py` following this pattern:

```python
@tool
def your_tool_name(param1: str, param2: int, param3: bool = False):
    """Your tool description here
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter  
        param3: Description of third parameter (optional)
    
    Returns:
        str: Description of what your tool returns
    """
    try:
        # Your tool implementation here
        result = f"Processed {param1} with {param2}"
        if param3:
            result += " (flag enabled)"
        return result
    except Exception as e:
        return f"Error: {str(e)}"
```

### 2. Tool Requirements

- **Use the `@tool` decorator**: This automatically registers your function
- **Type hints**: Add type hints for all parameters
- **Docstring**: Include clear description and parameter documentation
- **Error handling**: Always wrap in try/except blocks
- **Return strings**: Always return string values for consistency

### 3. Tool Examples

#### Simple Tool
```python
@tool
def greet_user(name: str, enthusiastic: bool = False):
    """Greets a user by name
    
    Args:
        name: The name to greet
        enthusiastic: Whether to use enthusiastic greeting
    """
    try:
        if enthusiastic:
            return f"Hello {name}! 🎉 It's great to see you!"
        else:
            return f"Hello {name}."
    except Exception as e:
        return f"Error: {str(e)}"
```

#### API Integration Tool
```python
@tool
def get_stock_price(symbol: str):
    """Gets current stock price for a symbol
    
    Args:
        symbol: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
    
    Returns:
        str: Current stock price or error message
    """
    try:
        import requests
        import os
        from dotenv import load_dotenv
        
        load_dotenv()
        api_key = os.getenv('STOCK_API_KEY')
        
        if not api_key:
            return "Error: STOCK_API_KEY not configured"
        
        # Example API call
        response = requests.get(
            f"https://api.example.com/stocks/{symbol}",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        
        if response.status_code == 200:
            data = response.json()
            price = data.get('price', 'N/A')
            return f"The current price of {symbol.upper()} is ${price}"
        else:
            return f"Error fetching stock data: {response.status_code}"
            
    except Exception as e:
        return f"Error: {str(e)}"
```

### 4. Testing Your Tool

After adding your tool, test it:

```python
# Test your tool directly
from tools import execute_tool

result = execute_tool("your_tool_name", {
    "param1": "test_value",
    "param2": 42,
    "param3": True
})
print(result)
```

Then test with the full agent:

```python
from engine import MicroAgent

agent = MicroAgent()
result = agent.run("Use your_tool_name with test_value, 42, and True")
print(result)
```

### 5. Best Practices

- **Keep it simple**: Tools should do one thing well
- **Handle errors gracefully**: Always return meaningful error messages
- **Use environment variables**: For API keys and configuration
- **Document everything**: Clear docstrings help users understand your tool
- **Test thoroughly**: Verify your tool works before submitting

### 6. Submitting Your Contribution

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-tool-name`
3. Add your tool to `src/tools.py`
4. Test your changes
5. Commit your changes: `git commit -m "Add: your_tool_name"`
6. Push your branch: `git push origin feature/your-tool-name`
7. Create a Pull Request

### 7. Tool Categories

Common tool categories for inspiration:

- **Information**: Search, fetch, retrieve data
- **Calculation**: Math, conversions, computations
- **Communication**: Email, notifications, messaging
- **File Operations**: Read, write, process files
- **System**: System information, configuration
- **External APIs**: Weather, stocks, databases, services

### 8. Getting Help

If you need help implementing a tool:

1. Check existing tools in `src/tools.py` for patterns
2. Look at the tool registry system in `src/tools.py`
3. Review the agent implementation in `src/engine.py`
4. Create an issue in the GitHub repository

---

Happy coding! 🚀
