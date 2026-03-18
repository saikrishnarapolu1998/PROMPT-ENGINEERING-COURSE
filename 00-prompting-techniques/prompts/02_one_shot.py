import sys
from pathlib import Path

# allow importing from the lesson module directory
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Rewrite  the sentence into a more professional business tone.

Example:
Input: Why isn't this done yet?
Output: Could you provide a quick status update on this task?

Now do the same for:
Input: Tell me what you think now.
Output:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)
