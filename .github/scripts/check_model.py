#!/usr/bin/env python3
"""
Check if the required Ollama model is available
Tenet 8: Your AI should never change in one project
"""

import subprocess
import sys
import json

def check_ollama_model(model_name: str = "deepseek-r1:8b") -> bool:
    """Check if the specified Ollama model is available"""
    try:
        # Check if Ollama is running
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=30)
        
        if result.returncode != 0:
            print(f"❌ Ollama not available: {result.stderr}")
            return False
        
        # Parse model list
        lines = result.stdout.strip().split('\n')
        models = [line.split()[0] for line in lines[1:] if line.strip()]  # Skip header
        
        if model_name in models:
            print(f"✅ Model {model_name} is available")
            return True
        else:
            print(f"❌ Model {model_name} not found. Available models: {', '.join(models)}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Ollama command timed out")
        return False
    except FileNotFoundError:
        print("❌ Ollama not installed")
        return False
    except Exception as e:
        print(f"❌ Error checking model: {e}")
        return False

if __name__ == "__main__":
    model_name = sys.argv[1] if len(sys.argv) > 1 else "deepseek-r1:8b"
    success = check_ollama_model(model_name)
    sys.exit(0 if success else 1)