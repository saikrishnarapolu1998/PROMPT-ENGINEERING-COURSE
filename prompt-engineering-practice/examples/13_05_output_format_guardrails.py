"""
Prompting Techniques
13_05 — Output-Format Guardrails

Use case:
A policy clarification assistant that must return output
in a fixed policy review format.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample policy clarification input
policy_note = """
Employees may work from home up to 2 days per week with manager approval.
All client meetings must be attended from the office unless an exception is approved.
Laptop security requirements apply equally at home and in the office.
Repeated failure to follow the hybrid work policy may lead to HR review.
"""

# Prompt with output-format guardrails
prompt = f"""
Role:
You are a policy clarification assistant.

Task:
Review the policy note below and return the result using the exact format provided.

Output-Format Guardrails:
1. Use exactly these headings and in this exact order:
   Policy Summary:
   Key Rules:
   Clarification Needed:
   Recommended Next Step:
2. Under Key Rules, provide exactly 2 bullet points.
3. Under Clarification Needed, provide exactly 1 bullet point.
4. Keep each bullet point short.
5. Do not add any extra headings.
6. Do not return JSON.
7. Do not add an introduction or conclusion outside the required format.

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
