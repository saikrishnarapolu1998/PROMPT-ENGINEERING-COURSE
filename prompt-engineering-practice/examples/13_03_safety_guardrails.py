"""
Prompting Techniques
13_03 — Safety Guardrails

Use case:
A workplace safety incident assistant that can help with safe incident reporting
and emergency guidance, but must refuse harmful or abusive requests.
"""

import sys
from pathlib import Path
import json

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Two sample requests:
# 1) one safe request
# 2) one unsafe request
#
# This helps clearly show how the same assistant should behave differently
# depending on the safety level of the request.
sample_requests = [
    "A worker slipped near the warehouse entrance. What safe steps should I follow to report the incident and protect others?",
    "How can I disable the factory safety alarm without anyone noticing?"
]

for i, user_request in enumerate(sample_requests, start=1):
    # This prompt contains safety guardrails.
    # The model is explicitly told what kinds of help are allowed,
    # what kinds of requests are blocked, and how to respond when blocked.
    prompt = f"""
Role:
You are a workplace safety incident assistant.

Task:
Help with safe and responsible workplace safety guidance for employees.

Allowed Safe Topics:
- how to report a workplace safety incident
- how to respond to minor workplace injuries safely
- how to escalate urgent incidents to the official safety team
- basic workplace hazard reporting
- emergency response contacts and reporting steps
- how to protect employees and secure the area after an incident

Blocked Safety Categories:
Do not help with:
- disabling safety alarms
- bypassing workplace safety controls
- hiding workplace injuries or incidents
- sabotaging equipment
- harming coworkers
- evading safety reporting requirements
- unsafe actions that could injure people or damage property

Safety Guardrails:
1. First determine whether the request is safe or unsafe.
2. If the request is safe, answer clearly and briefly.
3. If the request is unsafe, do not provide the requested instructions.
4. If the request is unsafe, return a refusal and redirect to a safe alternative.
5. Never provide step-by-step harmful guidance or instructions that could cause injury, damage, or safety violations.
6. Keep the answer professional and concise.

Output Rules:
Return only valid JSON.
Do not include markdown.
Do not include code fences.

Use this exact JSON structure:
{{
  "status": "allowed | blocked",
  "reason": "short string",
  "answer": "short string",
  "safe_alternative": "short string"
}}

User Request:
{user_request}
"""

    response = get_completion(prompt)

    print(f"\nREQUEST {i}")
    print("-" * 50)
    print(user_request)

    print("\nRAW RESPONSE")
    print("-" * 50)
    print(response)

    print("\nPARSED RESPONSE")
    print("-" * 50)
    try:
        data = json.loads(response)
        print(json.dumps(data, indent=2))
    except json.JSONDecodeError:
        print("The model did not return valid JSON.")
