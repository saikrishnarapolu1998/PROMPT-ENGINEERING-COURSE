"""
Prompting Techniques
Example: Zero-Shot vs One-Shot vs Few-Shot
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

simple_prompt = """
Explain the difference between zero-shot prompting, one-shot prompting, and few-shot prompting
for a complete beginner.

Use this format:
1. Zero-Shot Prompting
2. One-Shot Prompting
3. Few-Shot Prompting
4. Simple Comparison

Keep the explanation short, simple, and practical.
"""

response = get_completion(simple_prompt)

print("PROMPT:")
print("-" * 50)
print(simple_prompt)

print("\nMODEL EXPLANATION:")
print("-" * 50)
print(response)

print("\n" + "=" * 70)
print("IMPORTANT NOTE")
print("-" * 50)
print("Zero-shot prompting = giving no examples.")
print("One-shot prompting = giving one example.")
print("Few-shot prompting = giving a few examples to show the pattern.")
print("These are prompt design methods used at runtime.")
