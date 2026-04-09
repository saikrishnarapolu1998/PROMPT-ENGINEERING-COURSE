"""
Prompting Techniques
13_08 — Output Validation Guardrails

Use case:
An aviation incident note assistant that must return
a response in a required structure, and the output is validated after generation.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Incident information provided to the assistant
incident_note = """
During descent, the flight crew reported unusual vibration from the left engine.
The aircraft landed safely at Chennai International Airport.
No passenger injuries were reported.
Maintenance inspection was requested immediately after landing.
Weather conditions were clear at the time of arrival.
"""

# Prompt with required structure
prompt = f"""
Role:
You are an aviation incident note assistant.

Task:
Create a short aviation incident summary using the exact headings below.

Required Format:
Incident Type:
Location:
Severity:
Immediate Follow-Up:

Rules:
1. Use the exact headings shown above.
2. Keep each section short.
3. Do not add extra headings.
4. Do not add an introduction or conclusion.

Incident Information:
{incident_note}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the prompt
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print the raw response
print("\nRESPONSE:")
print("-" * 50)
print(response)

# Output validation guardrail:
# Check whether the model actually returned all required sections.
required_sections = [
    "Incident Type:",
    "Location:",
    "Severity:",
    "Immediate Follow-Up:"
]

missing_sections = [
    section for section in required_sections if section not in response
]

print("\nOUTPUT VALIDATION RESULT:")
print("-" * 50)

if not missing_sections:
    print("Validation passed: all required sections are present.")
else:
    print("Validation failed: missing sections found.")
    print("Missing:", ", ".join(missing_sections))
