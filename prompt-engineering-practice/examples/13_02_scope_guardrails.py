"""
Prompting Techniques
13_02 — Scope Guardrails

Use case:
A product return assistant that must answer only in-scope questions.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Policy text the assistant is allowed to use
return_policy = """
Product Return Policy:
- Customers can return products within 7 days of delivery.
- The product must be unused and in its original packaging.
- Damaged or defective products can be returned within 30 days.
- Refunds are processed within 5 business days after the return is approved.
- Final sale items cannot be returned.
"""

# We use two questions so students can clearly see in-scope vs out-of-scope behavior
sample_questions = [
    "Can I return a product if it is unused and delivered 5 days ago?",
    "Can you help me reset my account password?"
]

for i, user_question in enumerate(sample_questions, start=1):
    # Scope guardrails define what topic the assistant is allowed to handle
    prompt = f"""
Role:
You are a product return support assistant for an online store.

Task:
Answer the customer question only if it is within the allowed scope.

Allowed Scope:
You may answer only questions related to:
- product returns
- refund eligibility
- return timelines
- damaged or defective product returns
- return conditions and packaging requirements

Out-of-Scope Topics:
Do not answer questions related to:
- password reset
- account access
- shipping delays
- discount offers
- technical troubleshooting
- general customer support topics not related to returns

Scope Guardrails:
1. First decide whether the question is in scope or out of scope.
2. If it is in scope, answer using only the return policy below.
3. If it is out of scope, do not answer the question normally.
4. If it is out of scope, reply exactly with:
   "This question is outside the scope of the product return assistant. Please contact the appropriate support team."
5. Keep the answer short and clear.

Return Policy:
{return_policy}

Customer Question:
{user_question}
"""

    response = get_completion(prompt)
    print(response)
