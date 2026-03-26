"""
Prompting Techniques
Example: JSON Prompting for Structured Outputs
"""

import sys
from pathlib import Path
import json

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Generate a workout plan for a beginner who wants to get fitter at home.

Return only valid JSON.
Do not include markdown.
Do not include code fences.

Use this exact structure:
{
  "goal": "string",
  "fitness_level": "string",
  "days": [
    {
      "day": 1,
      "focus": "string",
      "workout": "string",
      "estimated_minutes": 0
    }
  ]
}

Rules:
- Create exactly 6 days
- Keep the language beginner-friendly
- Make each task realistic for 1 hour or less
- Focus on simple home workouts with no equipment
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nRaw Response:")
print("-" * 50)
print(response)

print("\nParsed JSON:")
print("-" * 50)

try:
    data = json.loads(response)
    print(json.dumps(data, indent=2))
except json.JSONDecodeError:
    print("The response was not valid JSON.")
