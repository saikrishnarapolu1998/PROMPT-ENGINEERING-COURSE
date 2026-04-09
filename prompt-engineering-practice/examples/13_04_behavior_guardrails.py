"""
Prompting Techniques
13_04 — Behavior Guardrails

Use case:
An HR communication drafting assistant that must communicate
in a clear, professional, and empathetic way.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# HR context provided to the assistant
hr_context = """
The company will conduct a mandatory workplace conduct training next Friday.
All employees are expected to attend.
Managers should ensure their teams complete the session.
Employees with scheduling conflicts should contact HR in advance.
"""

# Prompt with behavior guardrails
prompt = f"""
Role:
You are an HR communication drafting assistant.

Task:
Write a short internal HR communication based on the information below.

Behavior Guardrails:
1. Use a professional and empathetic tone.
2. Be clear and concise.
3. Do not use threatening or harsh language.
4. Do not make assumptions beyond the provided information.
5. Avoid sounding accusatory or judgmental.
6. Make the message respectful and easy for employees to understand.
7. End with a polite next-step or support line.

HR Information:
{hr_context}
"""

response = get_completion(prompt)

print("PROMPT:")
print("-" * 50)
print(prompt)

print("\nRESPONSE:")
print("-" * 50)
print(response)