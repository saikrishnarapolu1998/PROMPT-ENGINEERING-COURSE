# 04 Multi-Shot Prompting

## What it means

Multi-shot prompting is similar to few-shot prompting, but it usually means giving several examples to strongly guide the model.

## When to use it

Use it when the output format must be very consistent or when the task has many patterns.

## Small example

You show many examples of product descriptions before asking the model to write one in the same style.

## Example prompt

Example 1:
Product: Water bottle
Description: A lightweight bottle that is easy to carry and keeps your drink ready all day.

Example 2:
Product: Notebook
Description: A compact notebook for daily planning, quick notes, and simple organization.

Example 3:
Product: Desk lamp
Description: A practical lamp that gives focused light for study, reading, or work.

Now write a description for:
Product: Travel backpack

## Sample output

A durable backpack with enough space for daily travel, work items, and short trips while staying comfortable to carry.

## Key takeaway

More examples can make the model more reliable, but they also make the prompt longer.
