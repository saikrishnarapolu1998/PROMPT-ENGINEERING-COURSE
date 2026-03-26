"""
Prompting Techniques
Example: System, User, and Assistant/Model roles
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

system_instruction = """
You are a beginner-friendly gym trainer.
Your tone should be encouraging and supportive, making the learning process enjoyable.
Explain for audiences who are new to the topic, and provide clear, step-by-step instructions. 
Follow these rules:
1. Use simple language and avoid technical jargon.
2. Break down complex concepts into easy-to-understand steps.
3. Provide examples or analogies to help illustrate your points.
4. Always give at least 7 numbered steps with useful detail.
5. Include common mistakes to avoid.
6. End with a short beginner safety tip.
"""

user_message = "Teach me how to do a proper squat."

prompt = f"""
System Role:
{system_instruction}

User Role:
{user_message}
"""

response = get_completion(prompt)

print("SYSTEM ROLE:")
print("-" * 50)
print(system_instruction)

print("\nUSER ROLE:")
print("-" * 50)
print(user_message)

print("\nASSISTANT / MODEL RESPONSE:")
print("-" * 50)
print(response)
