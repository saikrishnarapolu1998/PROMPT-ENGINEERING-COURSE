"""
Prompting Techniques
16 — JSON Prompting for API Reliability

Use case:
An insurance claim routing assistant that returns
predictable JSON for workflow/API usage.
"""

import sys
from pathlib import Path
import json

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Insurance claim details
insurance_claim = """
Claim ID: CLM-2048
Policy Number: PL-88319
Claim Type: Auto
Incident Summary: Rear bumper damage after a minor collision in a parking area
Policy Status: Active
Documentation Status: Photos submitted, police report not required
Urgency: Customer needs claim review before repair scheduling
"""

# Prompt designed for reliable JSON output
prompt = f"""
Role:
You are an insurance claim routing assistant.

Task:
Read the insurance claim details below and return only valid JSON.

API Reliability Rules:
1. Return only valid JSON.
2. Do not include markdown.
3. Do not include code fences.
4. Use exactly these keys:
   "routing_status", "claim_type", "priority", "assigned_team", "next_action"
5. Use only one of these values for "routing_status":
   "route_to_adjuster", "needs_review", "reject"
6. Use only one of these values for "claim_type":
   "auto", "health", "property"
7. Use only one of these values for "priority":
   "low", "medium", "high"
8. Use only one of these values for "assigned_team":
   "auto_claims", "health_claims", "property_claims", "manual_review"
9. Keep "next_action" short and operational.

Return this exact JSON structure:
{{
  "routing_status": "route_to_adjuster | needs_review | reject",
  "claim_type": "auto | health | property",
  "priority": "low | medium | high",
  "assigned_team": "auto_claims | health_claims | property_claims | manual_review",
  "next_action": "string"
}}

Insurance Claim:
{insurance_claim}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the prompt
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print raw JSON response
print("\nRAW RESPONSE:")
print("-" * 50)
print(response)

# Parse JSON to verify API reliability
print("\nPARSED JSON:")
print("-" * 50)
parsed_claim_route = json.loads(response)
print(json.dumps(parsed_claim_route, indent=2))
