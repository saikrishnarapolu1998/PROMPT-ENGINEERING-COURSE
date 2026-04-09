"""
Prompting Techniques
17 — Safe Prompt Workflow with Constraints & Fallbacks

Use case:
Aviation incident routing assistant that must
respond safely, stay within limits, and use fallback behavior
when needed.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Incoming aviation incident message
incident_message = """
Flight ID: AX482
Location: Runway holding area
Reported Issue: Ground crew observed smoke near the left engine during pre-departure checks
Current Status: Aircraft remains on the ground and boarding is paused
Message: Please advise which team should handle this first and what the next safe step is.
"""

# Prompt with safe workflow rules
prompt = f"""
Role:
You are an aviation incident routing assistant.

Task:
Review the incident below and return a short safe routing response.

Constraints:
1. Do not invent facts that are not stated in the incident.
2. Do not issue technical maintenance instructions beyond safe routing guidance.
3. Do not claim the aircraft is safe or unsafe without sufficient information.
4. Keep the response short, clear, and operational.
5. Focus on incident severity, immediate routing, and the safest next step.

Fallback Rules:
1. If the incident suggests immediate operational danger, recommend immediate escalation to airport emergency response and ground operations.
2. If the incident is incomplete, ask for the single most important missing operational detail.
3. If the issue appears non-immediate, route to the most appropriate operational or maintenance team.
4. If you are uncertain, do not guess and state the uncertainty clearly.

Use this exact format:
Risk Level: ...
Route: ...
Next Step: ...

Incident:
{incident_message}
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
