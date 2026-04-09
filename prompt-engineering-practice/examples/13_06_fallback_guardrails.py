"""
Prompting Techniques
13_06 — Fallback Guardrails

Use case:
A policy clarification assistant that must
use fallback behavior when the request is unclear, ambiguous,
or requires HR or compliance review.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample policy-related input
policy_note = """
The remote work policy says employees may work from home with manager approval,
but it does not clearly explain whether employees can work remotely from another city
for two continuous weeks. The employee wants an immediate yes or no answer.
"""

# Prompt with fallback guardrails
prompt = f"""
Role:
You are a policy clarification assistant.

Task:
Review the policy note and provide a safe response.

Fallback Guardrails:
1. If the note is clear and low-risk, provide a short practical summary.
2. If the note is unclear or incomplete, ask for the missing information.
3. If the note appears sensitive, high-risk, or dependent on official approval, do not give a final approval answer.
4. In unclear or high-risk cases, recommend escalation to HR, compliance, or the policy owner.
5. Do not pretend certainty when important details are missing.
6. Keep the response short, professional, and action-oriented.

Use this exact format:
Decision: ...
Reason: ...
Next Step: ...

Policy Note:
{policy_note}
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
