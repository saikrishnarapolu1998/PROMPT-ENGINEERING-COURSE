import sys
from pathlib import Path

# allow importing from the lesson module directory
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
A student receives ₹15,000 per month from a part-time job.
Monthly expenses are ₹9,000.
The student wants to save ₹30,000 for a new phone.

Think step by step and answer:
1. How much the student saves each month
2. How many months are needed to save ₹30,000
3. One suggestion to reach the goal faster
"""


response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)
