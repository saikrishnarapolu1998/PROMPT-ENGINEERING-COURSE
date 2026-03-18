# Few-Shot Prompting

## What It Means

Few-shot prompting means giving the model multiple examples so it can learn the pattern before answering.

## In This Example

The prompt provides several examples of converting plain work statements into stronger resume bullet points. The model then writes a resume bullet for a new input.

## Why It Works

- Multiple examples show the pattern clearly.
- The rules define tone and structure.
- The model can imitate the style more reliably.

## Example Prompt

```text
Input: Worked on improving website speed and fixed some frontend bugs.
Resume Bullet: Improved website performance and resolved frontend bugs, enhancing user experience.
```

## Use Cases

- Resume bullet generation
- Classification
- Translation style control
- Structured rewriting
