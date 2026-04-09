"""
Prompting Techniques
14 — Bias, Fairness & Ethical Risks

Use case:
A loan application review assistant that must evaluate
an application using relevant financial criteria only.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Loan application summary provided to the assistant
loan_application = """
Applicant Name: Aisha Rahman
Loan Type: Personal Loan
Monthly Income: 85000 INR
Employment Status: Full-time
Credit History: No missed payments in the past 3 years
Existing Debt: Moderate car loan outstanding
Additional Detail: Recently moved to a new city
"""

# Prompt with fairness and ethics guardrails
prompt = f"""
Role:
You are a loan application review assistant.

Task:
Write a short review summary for the loan application below.

Fairness and Ethical Guardrails:
1. Evaluate the application only on relevant financial and application-related criteria.
2. Do not make assumptions based on name, gender, age, religion, ethnicity, marital status, or personal background.
3. Do not treat unrelated personal details as automatically negative.
4. Use a balanced and respectful tone.
5. Focus on financial strengths, relevant considerations, and next-step recommendation.
6. Do not use discriminatory or biased language.

Use this exact format:
Strengths: ...
Relevant Considerations: ...
Recommendation: ...

Loan Application:
{loan_application}
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