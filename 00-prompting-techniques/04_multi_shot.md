# Multi-Shot Prompting

## What It Means

Multi-shot prompting is a form of few-shot prompting where several examples are provided to reinforce the pattern strongly.

## In This Example

The prompt gives multiple product examples and their categories, then asks the model to tag a new product with one category only.

## Why It Works

- Repeated examples reduce ambiguity.
- The valid labels are explicitly listed.
- The task format stays consistent throughout.

## Example Prompt

```text
Tag each product with one category only:
Electronics, Clothing, Grocery, Furniture
```

## Use Cases

- Product category tagging
- Ticket routing
- Intent detection
- Label classification
