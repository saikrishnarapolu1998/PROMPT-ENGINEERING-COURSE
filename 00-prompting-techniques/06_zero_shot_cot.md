# Zero-Shot Chain-of-Thought Prompting

## What It Means

Zero-shot chain-of-thought prompting asks the model to reason step by step without giving any worked example first.

## In This Example

The prompt asks the model to calculate monthly savings, estimate how long a student will need to save for a phone, and suggest a faster way to reach the goal.

## Why It Works

- No examples are needed.
- The phrase asking for step-by-step thinking guides reasoning.
- The numbered tasks make the output easier to follow.

## Example Prompt

```text
Think step by step and answer:
1. How much the student saves each month
2. How many months are needed to save ₹30,000
3. One suggestion to reach the goal faster
```

## Use Cases

- Savings problems
- Word problems
- Estimation tasks
- Basic financial reasoning
