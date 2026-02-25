from llm_client import LLMClient
from tools import get_tool_metadata, execute_tool
import json

class MicroAgent:
    def __init__(self, max_iterations=5):
        self.llm = LLMClient()
        self.max_iterations = max_iterations
        self.history = []

    def run(self, goal: str):
        # System instructions force JSON and explain Thought/Action/Observation loop
        system_prompt = f"""You are a ReAct Agent. You must respond ONLY in JSON.
Available tools:
{get_tool_metadata()}

Format:
{{
  "thought": "Reason about what to do next",
  "action": "tool_name_or_null",
  "action_input": {{ "arg_name": "value" }},
  "final_answer": "your answer if finished, otherwise null"
}}"""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": goal}
        ]

        for i in range(self.max_iterations):
            print(f"Iteration {i+1}...")
            
            response_msg = self.llm.chat(messages)
            data = json.loads(response_msg["content"])
            
            print(f"Thought: {data['thought']}")

            if data["final_answer"]:
                return data["final_answer"]

            if data["action"]:
                print(f"Action: {data['action']}({data['action_input']})")
                result = execute_tool(data["action"], data["action_input"])
                print(f"Observation: {result}")
                
                # Log to history
                self.history.append({
                    "iteration": i + 1,
                    "thought": data['thought'],
                    "action": data['action'],
                    "action_input": data['action_input'],
                    "observation": result
                })
                
                # Update history: we add Assistant's thought AND Tool's result
                messages.append(response_msg)
                messages.append({
                    "role": "user", 
                    "content": f"Observation: {result}" 
                })
        
        return "Failed to reach answer within limits."
    
    def save_history(self, filename="history.json"):
        """Save execution trace to file"""
        with open(filename, "w") as f:
            json.dump(self.history, f, indent=2)
