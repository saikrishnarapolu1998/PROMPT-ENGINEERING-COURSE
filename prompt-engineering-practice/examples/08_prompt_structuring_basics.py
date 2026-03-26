"""
Prompting Techniques
Example: Prompt Structuring Basics
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Role:
You are a beginner-friendly business coach.

Task:
Suggest 5 simple business ideas for someone who wants to start a small business.

Context:
The person was recently laid off and has a very low budget.
They can work only part-time and want ideas that are easy to start and don't require a large initial investment.

Constraints:
- Use simple language
- Keep the ideas realistic and actionable
- Avoid ideas that require specialized skills or certifications
- Avoid ideas that need a lot of money
- Explain each idea in 1-2 lines
- Focus on beginner-friendly ideas that can be started with minimal resources

Output Format:
Return the answer in this format:

Idea 1: ...
Why it is good: ...
Idea 2: ...
Why it is good: ...
Idea 3: ...
Why it is good: ...
Idea 4: ...
Why it is good: ...
Idea 5: ...
Why it is good: ...
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)
