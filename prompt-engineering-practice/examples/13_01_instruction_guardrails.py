"""
Prompting Techniques
13_01 — Instruction Guardrails

Use case:
A leave policy assistant that must follow clear instructions.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample policy text that the model is allowed to use
leave_policy = """
Leave Policy:
- Employees are entitled to 18 paid leave days per year.
- Casual leave can be taken for up to 3 consecutive days.
- Sick leave requires a medical certificate if it exceeds 2 consecutive days.
- Unused paid leave cannot be carried forward to the next year.
- Leave requests must be submitted at least 2 days in advance unless it is an emergency.
"""
# Sample customer query
employee_question = """
I want to take 5 casual leave days in a row next week. Is that allowed?
"""

# Prompt with instruction guardrails
# These rules tell the model exactly how it should behave.
prompt = f"""
Role:
You are an HR leave policy assistant for a company.

Task:
Answer the employee question using only the leave policy provided below.

Instruction Guardrails:
1. Use only the information from the policy text.
2. Do not invent any new company rules.
3. If the policy does not clearly answer the question, say:
   "Please contact HR for clarification."
4. Keep the answer short and clear.
5. Use a polite professional tone.
6. End with one next-step suggestion for the employee.

Leave Policy:
{leave_policy}

Employee Question:
{employee_question}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the prompt so students can see the full structure
# print("PROMPT:")
# print("-" * 50)
# print(prompt)

# Print the model response
# print("\nRESPONSE:")
# print("-" * 50)
print(response)