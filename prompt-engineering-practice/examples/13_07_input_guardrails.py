"""
Prompting Techniques
13_07 — Input Guardrails

Use case:
A gaming abuse report intake assistant that checks input
before sending it to the model.
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample input
player_id = "Player8472"
game_mode = "Ranked Match"
report_summary = "The player used abusive language repeatedly in voice chat."
severity = "high"

# Input guardrails:
# We check the input first before calling the model.
if not player_id.strip():
    print("Blocked: player_id is required.")

elif not game_mode.strip():
    print("Blocked: game_mode is required.")

elif not report_summary.strip():
    print("Blocked: report_summary is required.")

elif severity.lower() not in ["low", "medium", "high", "critical"]:
    print("Blocked: severity must be low, medium, high, or critical.")

else:
    # Build the prompt only if the input passes validation
    prompt = f"""
Role:
You are a gaming abuse report intake assistant.

Task:
Convert the intake details below into a short internal moderation summary.

Rules:
1. Use only the details provided.
2. Keep the summary short and clear.
3. Do not guess intent or make accusations beyond the report.
4. Recommend the next intake route based on severity.

Use this format:
Player ID: ...
Game Mode: ...
Severity: ...
Report Summary: ...
Recommended Intake Route: ...

Validated Intake Details:
Player ID: {player_id}
Game Mode: {game_mode}
Report Summary: {report_summary}
Severity: {severity}
"""

    response = get_completion(prompt)

    print("PROMPT:")
    print("-" * 50)
    print(prompt)

    print("\nRESPONSE:")
    print("-" * 50)
    print(response)
