"""
Module 01 — Prompting Guidelines
Example: Zero-shot prompting
"""

import sys
from pathlib import Path

# allow importing from the lesson module directory
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Rewrite  the following paragraph in 5 simple bullet points for a beginner:

Artificial Intelligence (AI) refers to the development of computer systems capable of performing tasks that typically require human intelligence, such as reasoning, learning, problem-solving, and understanding language. Far from being mere science fiction, AI is an engine behind modern innovation, acting as a transformative technology in our daily lives. It encompasses various disciplines, including machine learning and deep learning, which enable machines to identify patterns and make predictions without being explicitly programmed for every scenario.
AI is integrated into daily routines to enhance convenience. Examples include personalized recommendations on streaming platforms, navigation apps, and virtual assistants. In healthcare, AI helps diagnose diseases earlier. In transportation, it powers self-driving features. These applications increase efficiency and minimize repetitive tasks.
Generative AI can create new content, including text, images, and code, in response to user prompts. Foundation models, such as Large Language Models (LLMs), have allowed machines to mimic human-like creativity and reasoning. This technology is shifting AI from an analytical tool to a collaborative partner, opening possibilities for augmented creativity in marketing, education, and entertainment.
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)
