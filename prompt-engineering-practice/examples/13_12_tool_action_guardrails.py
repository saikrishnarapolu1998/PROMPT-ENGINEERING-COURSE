"""
Prompting Techniques
13_12 — Tool / Action Guardrails

Use case:
A cloud access request assistant that must follow
action limits before recommending operational steps.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample support request
support_request = """
An employee says they need immediate access to the production cloud storage bucket
to support a live deployment. They are asking for urgent approval.
"""

# Prompt with tool / action guardrails
prompt = f"""
Role:
You are a cloud access request assistant.

Task:
Review the support request and respond using the exact format below.

Tool / Action Guardrails:
1. You may recommend safe actions such as submitting an access request or contacting the approved cloud admin.
2. Do not claim that you directly granted access.
3. Do not claim that you directly changed cloud permissions.
4. Do not invent any system action that was not actually performed.
5. If access requires approval, identity verification, or manager authorization, clearly say so.
6. Keep the response short, professional, and operationally clear.

Use this exact format:
Allowed Action: ...
Blocked Action: ...
Next Step: ...

Support Request:
{support_request}
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
