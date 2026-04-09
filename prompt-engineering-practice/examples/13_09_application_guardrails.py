"""
Prompting Techniques
13_09 — Application-Level Guardrails

Use case:
A banking support note assistant where the application
redacts sensitive details before sending text to the model.
"""

import sys
from pathlib import Path
import re

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Raw message received by the application
raw_message = """
Customer Name: Priya Sharma
Phone: 9876543210
Email: priya.sharma@example.com
Account Number: 123456789012
Branch: Chennai Main Branch
Message: The customer reported that an ATM cash withdrawal failed,
but the account was debited. The customer wants to know the next support step.
"""

# Application-level guardrail:
# redact sensitive fields before the model sees the message
sanitized_message = re.sub(r"Customer Name:.*", "Customer Name: [REDACTED]", raw_message)
sanitized_message = re.sub(r"Phone:.*", "Phone: [REDACTED]", sanitized_message)
sanitized_message = re.sub(r"Email:.*", "Email: [REDACTED]", sanitized_message)
sanitized_message = re.sub(r"Account Number:.*", "Account Number: [REDACTED]", sanitized_message)

# Prompt built only from the sanitized message
prompt = f"""
Role:
You are a banking support note assistant.

Task:
Summarize the following customer-support message into a short internal note.

Rules:
1. Use only the sanitized message below.
2. Keep the summary short and professional.
3. Do not provide financial advice.
4. Focus only on the operational follow-up needed.

Sanitized Message:
{sanitized_message}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the original message
print("RAW MESSAGE:")
print("-" * 50)
print(raw_message)

# Print the sanitized version used by the application
print("\nSANITIZED MESSAGE:")
print("-" * 50)
print(sanitized_message)

# Print the final response
print("\nMODEL RESPONSE:")
print("-" * 50)
print(response)
