import sys
from pathlib import Path

# allow importing from the lesson module directory
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Rewrite the input into a strong resume bullet point.

Rules:
- Start with an action verb
- Be concise and professional
- Focus on impact and results
- Use past tense for past work
- Do not use first person pronouns

Input: Worked on improving website speed and fixed some frontend bugs.
Resume Bullet: Improved website performance and resolved frontend bugs, enhancing user experience.

Input: Helped the team organize customer data in spreadsheets.
Resume Bullet: Organized customer data in spreadsheets, improving accuracy and team accessibility.

Input: Created social media posts for the company’s Instagram page.
Resume Bullet: Developed engaging Instagram content to support the company’s social media presence.

Input: I was responsible for answering customer emails and solving their issues.
Resume Bullet:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)
