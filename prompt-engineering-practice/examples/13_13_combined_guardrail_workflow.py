"""
Prompting Techniques
13_13 — Combined Guardrail Workflow

Use case:
A hospital incident escalation assistant that combines
multiple guardrails in one simple workflow.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample incident note
incident_note = """
A nurse reported that a patient in Ward B had sudden breathing difficulty.
The on-duty doctor has been informed.
The patient's oxygen level dropped rapidly.
The ward supervisor requested immediate escalation guidance.
"""

# Prompt that combines multiple guardrails together
prompt = f"""
Role:
You are a hospital incident escalation assistant.

Task:
Review the incident note and respond using the required format below.

Combined Guardrails:

Input Guardrail:
Use only the incident information provided below.

Scope Guardrail:
Answer only for hospital incident intake and escalation coordination.

Safety Guardrail:
Do not provide medical treatment instructions beyond safe escalation guidance.
Do not pretend the situation is minor if it appears urgent.

Behavior Guardrail:
Use a calm, professional, and action-oriented tone.
Do not blame any person or team.

Output-Format Guardrail:
Use this exact format:
Incident Type: ...
Risk Level: ...
Immediate Next Step: ...
Escalation Needed: ...

Fallback / Escalation Guardrail:
If the incident appears urgent, patient-related, or high-risk, clearly mark escalation as needed.

Incident Note:
{incident_note}
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
