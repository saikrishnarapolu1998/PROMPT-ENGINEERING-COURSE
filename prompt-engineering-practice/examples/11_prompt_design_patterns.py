"""
Prompting Techniques
Example: Prompt Design Patterns
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

email_text = """
Hi John,

I hope you are doing well. I wanted to check if we can reschedule tomorrow's meeting to Friday afternoon.
I have a client call at the same time, so I will not be able to attend.
Please let me know if Friday at 3 PM works for you.

Thanks,
Sai
"""

# Pattern 1: Classification
classification_prompt = f"""
Classify the tone of the following email as Formal, Informal, or Neutral.

Email:
{email_text}
"""

# Pattern 2: Extraction
extraction_prompt = f"""
Extract the following details from the email.

Return the answer in this format:
- Sender Intent:
- Main Request:
- Important Date or Time:
- Action Needed:

Email:
{email_text}
"""

# Pattern 3: Transformation
transformation_prompt = f"""
Rewrite the following email in a more professional tone.

Email:
{email_text}
"""

# Pattern 4: Generation
generation_prompt = f"""
Based on the following email, generate a polite reply.

Email:
{email_text}
"""

classification_response = get_completion(classification_prompt)
extraction_response = get_completion(extraction_prompt)
transformation_response = get_completion(transformation_prompt)
generation_response = get_completion(generation_prompt)

print("PATTERN 1 — CLASSIFICATION")
print("-" * 50)
print(classification_response)

print("\nPATTERN 2 — EXTRACTION")
print("-" * 50)
print(extraction_response)

print("\nPATTERN 3 — TRANSFORMATION")
print("-" * 50)
print(transformation_response)

print("\nPATTERN 4 — GENERATION")
print("-" * 50)
print(generation_response)
