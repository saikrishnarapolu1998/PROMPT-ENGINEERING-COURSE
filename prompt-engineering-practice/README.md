# Prompt Engineering Practice

Beginner-friendly practice project for learning prompt engineering with simple Python examples and short notes.

## Topics Covered

- Zero-shot prompting
- One-shot prompting
- Few-shot prompting
- Multi-shot prompting
- Chain-of-thought prompting
- Zero-shot chain-of-thought
- System, user, and assistant roles
- Prompt structuring basics
- Prompt reuse and versioning
- Output formatting
- Prompt debugging
- Prompt tuning vs instruction tuning

## Setup Steps

```bash
cd /Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

Create `.env` in the project folder and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

## How To Run Example Files

Run any practice file from the project folder:

```bash
cd /Users/saikrishna/Desktop/prompt-engineering-course/prompt-engineering-practice
./.venv/bin/python examples/08_prompt_structuring_basics.py
```

You can replace the filename with any other file inside `examples/`.

## Folder Structure

```text
prompt-engineering-practice/
├── .env
├── .gitignore
├── .venv/
├── requirements.txt
├── helper.py
├── README.md
├── examples/
├── prompts/
└── assignments/
```

- `examples/` contains runnable Python example files
- `prompts/` contains topic notes in Markdown
- `assignments/` contains assignment files in Markdown
