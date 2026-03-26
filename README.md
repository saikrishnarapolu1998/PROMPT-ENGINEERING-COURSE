# Prompt Engineering Course

This repository showcases beginner-friendly prompt engineering practice using Python and Gemini-compatible prompts. It is organized as a small portfolio project that demonstrates common prompting patterns, runnable examples, and short written notes.

## What Recruiters Can See Quickly

- Practical prompt engineering examples, not just theory
- Runnable Python scripts for each prompting concept
- Clear lesson notes with sample prompts and sample outputs
- Structured project layout with examples, prompts, and assignments

## Main Project

The active project is inside [`prompt-engineering-practice`](/Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice).

Inside it, you will find:

- [`examples/`](/Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice/examples) for runnable Python files
- [`prompts/`](/Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice/prompts) for short topic notes with example outputs
- [`assignments/`](/Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice/assignments) for practice tasks
- [`README.md`](/Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice/README.md) for setup and execution instructions

## Topics Covered

- Zero-shot prompting
- One-shot prompting
- Few-shot prompting
- Multi-shot prompting
- Chain-of-thought prompting
- Zero-shot chain-of-thought prompting
- System, user, and assistant roles
- Prompt structuring basics
- Prompt reuse and versioning
- Output formatting
- Prompt debugging
- Prompt tuning vs instruction tuning

## Quick Start

```bash
cd prompt-engineering-practice
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

Then add a `.env` file in `prompt-engineering-practice/`:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

Run an example:

```bash
cd prompt-engineering-practice
./.venv/bin/python examples/01_zero_shot.py
```

## Repository Goal

This repository is meant to demonstrate understanding of prompt design fundamentals through simple, readable examples that can be reviewed quickly by recruiters, hiring managers, and other learners.
