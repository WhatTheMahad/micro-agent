import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from engine import MicroAgent

def main():
    agent = MicroAgent()
    
    # Example 1: Weather query
    print("=" * 50)
    print("EXAMPLE 1: Weather Query")
    print("=" * 50)
    result = agent.run("What's the weather like in Cape Town?")
    
    # Example 2: Math calculation
    print("\n" + "=" * 50)
    print("EXAMPLE 2: Math Calculation")
    print("=" * 50)
    agent2 = MicroAgent()
    result = agent2.run("Calculate (15 * 7) + 93-12")
    
    # Save trace
    agent2.save_history()
    print("\n✓ Execution trace saved to history.json")

if __name__ == "__main__":
    main()
