"""
Prompting Techniques
Example: Prompt Reuse and Versioning
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

target_audience = "a college student with a very small budget"
budget = "under $200"
time_available = "10 hours per week"
goal = "start a simple side business"

# Version 1: very basic prompt
prompt_v1 = f"""
Suggest 5 business ideas for {target_audience}.
"""

# Version 2: improved prompt with more clarity
prompt_v2 = f"""
Role:
You are a beginner-friendly small business coach.

Task:
Suggest 5 business ideas for someone who wants to {goal}.

Context:
The person is {target_audience}.
They can invest only {budget}.
They have only {time_available}.

Constraints:
- Use simple language
- Keep the ideas realistic and practical
- Focus on low-cost ideas
- Avoid ideas that require advanced technical skills
- Avoid ideas that need licenses, certifications, or a large team
- Explain each idea in 1-2 lines

Output Format:
Idea 1: ...
Why it fits: ...
Idea 2: ...
Why it fits: ...
Idea 3: ...
Why it fits: ...
Idea 4: ...
Why it fits: ...
Idea 5: ...
Why it fits: ...
"""

response_v1 = get_completion(prompt_v1)
response_v2 = get_completion(prompt_v2)

print("PROMPT VERSION 1")
print("-" * 50)
print(prompt_v1)

print("\nRESPONSE VERSION 1")
print("-" * 50)
print(response_v1)

print("\n" + "=" * 70 + "\n")

print("PROMPT VERSION 2")
print("-" * 50)
print(prompt_v2)

print("\nRESPONSE VERSION 2")
print("-" * 50)
print(response_v2)
