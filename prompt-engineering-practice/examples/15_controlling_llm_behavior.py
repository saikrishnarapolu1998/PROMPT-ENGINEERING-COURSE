"""
Prompting Techniques
15 — Controlling LLM Behavior

Use case:
A hospital operations update assistant that must communicate
in a short, neutral, operations-focused style.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Hospital operations update information
update_note = """
Emergency department wait times decreased by 18% this week.
The ICU is operating at 92% capacity.
Two ventilators were returned to service after maintenance.
Night-shift staffing remains tight in the surgical ward.
An additional nurse onboarding group starts next Monday.
"""

# Prompt that controls model behavior
prompt = f"""
Role:
You are a hospital operations update assistant.

Task:
Write a short hospital operations update for leadership based on the information below.

Behavior Controls:
1. Use a formal and professional tone.
2. Keep the response concise.
3. Focus on operational impact, progress, capacity, and risk.
4. Do not use clinical jargon unless necessary.
5. Do not sound casual or conversational.
6. Keep the message neutral and factual.
7. End with one short forward-looking line.

Update Information:
{update_note}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the prompt
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print the response
print("\nRESPONSE:")
print("-" * 50)
print(response)
