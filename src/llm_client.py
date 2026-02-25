import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables at module level
load_dotenv()

class LLMClient:
    def __init__(self):
        self.base_url = os.getenv("LLM_BASE_URL")
        self.model = os.getenv("LLM_MODEL")

    def chat(self, messages):
        """Standardized chat interface using Ollama's /api/chat endpoint"""
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "format": "json"  # Forces model to output valid JSON
        }
        
        print(f"Using model: {self.model}")  # Debug output
        
        response = requests.post(f"{self.base_url}/api/chat", json=payload)
        
        if response.status_code != 200:
            raise Exception(f"Ollama Error: {response.text}")
            
        return response.json()["message"]
