# Prompt Engineering Practice

This project demonstrates core prompt engineering concepts through simple Python examples, short lesson notes, and practice assignments. It is designed to be easy to review quickly while still showing practical prompting work.

## What This Project Includes

- Runnable prompt engineering examples in Python
- Short notes for each concept
- Example prompts and sample outputs in the notes
- Practice assignments for each topic
- Local mock responses when no Gemini API key is configured

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
- Instruction, scope, safety, and behavior guardrails
- Output validation, fallback handling, escalation, privacy, and tool action guardrails
- Bias, fairness, and ethical risk reduction
- Controlling LLM behavior with explicit style constraints
- JSON prompting for reliable workflow or API outputs
- Safe prompt workflows with operational limits and fallback behavior

## Project Structure

```text
prompt-engineering-practice/
├── assignments/
├── examples/
├── prompts/
├── helper.py
├── README.md
└── requirements.txt
```

- [`examples/`](/Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice/examples) contains runnable Python files
- [`prompts/`](/Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice/prompts) contains notes, example prompts, and sample outputs
- [`assignments/`](/Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice/assignments) contains practice tasks
- [`helper.py`](/Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice/helper.py) handles Gemini calls and local fallback responses

The `prompts/` folder currently covers lessons `01` through `12`.
The `examples/` folder continues beyond that with advanced runnable examples from `13_01` through `17`.

## Setup

```bash
cd /Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

Create `.env` in the project folder:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

If `GEMINI_API_KEY` is missing, the project still runs using local demo responses so the examples remain reviewable.

## How To Run

```bash
cd /Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice
./.venv/bin/python examples/01_zero_shot.py
```

Replace the filename with any file from [`examples/`](/Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice/examples).

Examples you can try next:

- `examples/13_01_instruction_guardrails.py`
- `examples/13_13_combined_guardrail_workflow.py`
- `examples/14_bias_fairness_ethical_risks.py`
- `examples/15_controlling_llm_behavior.py`
- `examples/16_json_prompting_api_reliability.py`
- `examples/17_safe_prompt_workflow_constraints_fallbacks.py`

## Suggested Review Path

If someone is visiting this repository for the first time, the fastest way to review it is:

1. Read this README.
2. Open a few files in [`prompts/`](/Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice/prompts) to see the concept, sample prompt, and sample output.
3. Open the matching script in [`examples/`](/Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice/examples) to see the runnable implementation.
4. Check [`assignments/`](/Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice/assignments) for hands-on practice items.
