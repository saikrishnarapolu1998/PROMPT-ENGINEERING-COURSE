import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


def load_env_file(env_path=None):
    path = Path(env_path) if env_path else PROJECT_ROOT / ".env"
    if not path.exists():
        return

    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


load_env_file()


def _mock_response(prompt):
    lower_prompt = prompt.lower()

    if "generate a workout plan" in lower_prompt and "return only valid json" in lower_prompt:
        return """{
  "goal": "Get fitter at home",
  "fitness_level": "Beginner",
  "days": [
    {
      "day": 1,
      "focus": "Light full-body movement",
      "workout": "10 squats, 8 wall push-ups, 20-second plank, and a 10-minute walk",
      "estimated_minutes": 25
    },
    {
      "day": 2,
      "focus": "Core and mobility",
      "workout": "15 glute bridges, 20-second side planks on both sides, gentle stretching, and a 10-minute walk",
      "estimated_minutes": 20
    },
    {
      "day": 3,
      "focus": "Beginner cardio and legs",
      "workout": "3 rounds of 15 marching steps, 10 lunges, 10 sit-to-stands, and 5 minutes of stretching",
      "estimated_minutes": 30
    },
    {
      "day": 4,
      "focus": "Upper body basics",
      "workout": "10 wall push-ups, 12 arm circles, 15 shoulder taps, and 5 minutes of stretching",
      "estimated_minutes": 20
    },
    {
      "day": 5,
      "focus": "Lower body strength",
      "workout": "12 squats, 10 lunges on each leg, 15 calf raises, and a 10-minute walk",
      "estimated_minutes": 30
    },
    {
      "day": 6,
      "focus": "Light cardio and recovery",
      "workout": "15 minutes of brisk walking, 10 marching steps, and full-body stretching",
      "estimated_minutes": 25
    }
  ]
}"""

    if "system role:" in lower_prompt and "teach me how to do a proper squat" in lower_prompt:
        return """[Local demo mode: no Gemini API key configured]

1. Stand with your feet about shoulder-width apart and keep your chest up.
2. Tighten your core so your back stays stable during the movement.
3. Push your hips back first, as if you are sitting into a chair.
4. Bend your knees and lower your body slowly while keeping your heels on the floor.
5. Go down only as far as you can while keeping your back straight and your knees comfortable.
6. Press through your heels to stand back up in a controlled way.
7. Repeat slowly and focus on balance, posture, and breathing.

Common mistakes to avoid: letting your knees collapse inward, lifting your heels, or rounding your back.
Safety tip: Start with bodyweight only and stop if you feel knee or back pain."""

    if "classify the tone of the following email" in lower_prompt:
        return """[Local demo mode: no Gemini API key configured]

Formal"""

    if "extract the following details from the email" in lower_prompt:
        return """[Local demo mode: no Gemini API key configured]

- Sender Intent: To reschedule a meeting
- Main Request: Move the meeting from tomorrow to Friday afternoon
- Important Date or Time: Friday at 3 PM
- Action Needed: Confirm whether the new meeting time works"""

    if "rewrite the following email in a more professional tone" in lower_prompt:
        return """[Local demo mode: no Gemini API key configured]

Hi John,

I hope you are doing well. I would like to request rescheduling tomorrow's meeting to Friday afternoon, as I have a client call at the same time and will be unable to attend.

Please let me know if Friday at 3 PM is convenient for you.

Thank you,
Sai"""

    if "based on the following email, generate a polite reply" in lower_prompt:
        return """[Local demo mode: no Gemini API key configured]

Hi Sai,

Thank you for the update. Friday at 3 PM works for me, and we can move the meeting to that time.

Best regards,
John"""

    if "zero-shot prompting" in lower_prompt and "few-shot prompting" in lower_prompt and "simple comparison" in lower_prompt:
        return """[Local demo mode: no Gemini API key configured]

1. Zero-Shot Prompting
Zero-shot prompting means asking the model to do a task without giving any example first.

2. One-Shot Prompting
One-shot prompting means giving one example so the model can understand the pattern.

3. Few-Shot Prompting
Few-shot prompting means giving a few examples before the real task to improve consistency.

4. Simple Comparison
The difference is the number of examples you give: none, one, or a few."""

    if "suggest 5 business ideas for" in lower_prompt and "why it fits" not in lower_prompt:
        return """[Local demo mode: no Gemini API key configured]

Idea 1: Handmade greeting cards
Idea 2: Study notes resale
Idea 3: Snack box delivery for students
Idea 4: Basic social media posting service
Idea 5: Used book flipping"""

    if "why it fits" in lower_prompt and "business ideas" in lower_prompt:
        return """[Local demo mode: no Gemini API key configured]

Idea 1: Custom gift basket service
Why it fits: It can be started from home with a small budget and marketed through friends and social media.

Idea 2: Campus poster and flyer design
Why it fits: Students and clubs often need low-cost design help, and basic tools are enough to begin.

Idea 3: Local snack resale
Why it fits: Buying in small bulk and selling near campus is simple and does not require advanced skills.

Idea 4: Social media help for small shops
Why it fits: Many local businesses need simple content posting support that can be done part-time.

Idea 5: Second-hand book resale
Why it fits: It is affordable to start and works well for students who understand what other students need."""

    if "5 simple business ideas" in lower_prompt:
        return """[Local demo mode: no Gemini API key configured]

Idea 1: Home-cooked snack orders
Why it is good: It can be started from home with very little money and simple equipment.

Idea 2: Local errand service
Why it is good: It is easy to begin part-time and helps busy people with shopping or small tasks.

Idea 3: Resume writing support
Why it is good: Many job seekers need basic help, and the startup cost is almost zero.

Idea 4: Social media posting for small shops
Why it is good: Small businesses often need simple posting help and you can start with a phone.

Idea 5: Used item resale
Why it is good: You can start small by finding low-cost items and reselling them for profit online."""

    if "5-day learning plan" in lower_prompt:
        return """[Local demo mode: no Gemini API key configured]

Day 1: Learn what prompt engineering is and read a few simple examples.
Day 2: Practice zero-shot, one-shot, and few-shot prompting with short tasks.
Day 3: Compare weak prompts and improved prompts to see what changed.
Day 4: Practice structured prompts using role, task, context, constraints, and output format.
Day 5: Build 3 small prompts for real use cases and refine them based on the results."""

    return """[Local demo mode: no Gemini API key configured]

This example ran without calling Gemini.
The prompt was loaded correctly, but the response is a local placeholder.
Add GEMINI_API_KEY to .env to get a real model-generated answer."""


def get_completion(prompt, model=None):
    try:
        from google import genai
    except ImportError as exc:
        return _mock_response(prompt)

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return _mock_response(prompt)

    selected_model = model or os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=selected_model,
        contents=prompt,
    )
    return response.text
