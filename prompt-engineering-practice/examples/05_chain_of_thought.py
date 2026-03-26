import sys
from pathlib import Path

# allow importing from the lesson module directory
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
A person has to decide how to use 3 free hours in the evening:
exercise, study, or spend time with family.

Think step by step and answer:
1. What are the pros of each option?
2. What are the cons of each option?
3. Which option should the person choose?
4. Why?
"""


response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)
