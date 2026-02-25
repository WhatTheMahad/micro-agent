import inspect
from typing import Callable, Dict, List
from simpleeval import simple_eval  # Safe alternative to eval()

TOOL_REGISTRY: Dict[str, Callable] = {}

def tool(func: Callable):
    TOOL_REGISTRY[func.__name__] = func
    return func

def get_tool_metadata() -> str:
    """Returns a string description of tools for system prompt"""
    docs = []
    for name, func in TOOL_REGISTRY.items():
        sig = inspect.signature(func)
        docs.append(f"Tool: {name}{sig}\nDoc: {func.__doc__}")
    return "\n\n".join(docs)

@tool
def calculate(expression: str):
    """Safely evaluates a math expression (e.g. '15 * 2 + 10')"""
    try:
        return simple_eval(expression)
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def get_weather(city: str):
    """Returns weather for a specific city"""
    try:
        # Use WeatherAPI.com
        import requests
        import os
        from dotenv import load_dotenv
        
        # Load environment variables from .env file
        load_dotenv()
        
        # Get API key from environment
        api_key = os.getenv('WEATHERAPI_KEY')
        if not api_key:
            return "Error: WEATHERAPI_KEY not set in environment variables"
        
        # WeatherAPI.com endpoint
        BASE_URL = "https://api.weatherapi.com/v1/current.json"
        
        # Get weather data (WeatherAPI.com can search by city name directly)
        weather_url = f"{BASE_URL}?key={api_key}&q={city}&aqi=no"
        weather_response = requests.get(weather_url)
        
        # Debug: Check API response
        if weather_response.status_code != 200:
            return f"Weather API error: {weather_response.status_code} - {weather_response.text}"
        
        weather_data = weather_response.json()
        
        if weather_data.get('current'):
            temp = weather_data['current']['temp_f']
            condition = weather_data['current']['condition']['text']
            return f"The weather in {city.title()} is {condition}, {temp:.0f}°F"
        else:
            return f"Weather data unavailable for {city}"
            
    except Exception as e:
        return f"Error getting weather: {str(e)}"

def execute_tool(name: str, args: dict):
    if name not in TOOL_REGISTRY:
        return f"Error: Tool {name} not found"
    return TOOL_REGISTRY[name](**args)
