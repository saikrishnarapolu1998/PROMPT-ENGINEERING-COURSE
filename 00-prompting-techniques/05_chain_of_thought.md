# Chain-of-Thought Prompting

## What It Means

Chain-of-thought prompting encourages the model to reason through a problem step by step before giving the final answer.

## In This Example

The prompt asks the model to compare three evening choices: exercise, study, or spending time with family. It then evaluates pros, cons, and the best decision.

## Why It Works

- The task is broken into smaller questions.
- The model is guided to reason before concluding.
- The final answer becomes more structured and explainable.

## Example Prompt

```text
Think step by step and answer:
1. What are the pros of each option?
2. What are the cons of each option?
3. Which option should the person choose?
4. Why?
```

## Use Cases

- Decision-making
- Problem solving
- Scenario analysis
- Multi-step reasoning
