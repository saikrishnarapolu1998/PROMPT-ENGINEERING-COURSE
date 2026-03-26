# 03 Few-Shot Prompting

## What it means

Few-shot prompting means you give the model a few examples so it can learn the format or style you want.

## When to use it

Use it when the task is a little tricky or when consistency matters.

## Small example

You provide three examples of customer reviews labeled as positive or negative, then ask the model to label a new review.

## Example prompt

Review: "The food was fresh and the service was quick."
Label: Positive

Review: "The room was dirty and the staff was rude."
Label: Negative

Review: "The delivery was late but the product quality was good."
Label: Mixed

Now label this review:
"The app is easy to use, but it crashes sometimes."

## Sample output

Label: Mixed

## Key takeaway

More examples usually help the model follow your pattern better.
