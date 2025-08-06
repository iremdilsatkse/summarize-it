import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

# 1. Title + Summary (Gemini output in Turkish)


def summarize_text(text):
    prompt = f"""
You are an assistant that summarizes YouTube video transcripts.

Instructions:
- Generate a short and catchy title in **Turkish**, no more than 10 words.
- Then generate a **summary in Turkish**, max 250 words.
- Respond only in this format:

Title: <Turkish title>
Summary: <Turkish summary>

Transcript:
{text}
"""
    response = model.generate_content(prompt)
    result = response.text.strip()

    try:
        title = re.search(r"Title:\s*(.+)", result).group(1).strip()
        summary = re.search(r"Summary:\s*(.+)", result,
                            re.DOTALL).group(1).strip()
    except Exception as e:
        print("Başlık/özet ayrıştırılamadı:", e)
        title = "Başlık çıkarılamadı"
        summary = result

    return title, summary


# 2. Highlights
def generate_highlights(transcript):
    prompt = f"""
You are an assistant that finds key moments in a video transcript.

Instructions:
- Identify the 5 most important moments from the transcript.
- For each, return a Turkish short description and approximate timestamp in this format:

[00:MM:SS] Açıklama

Only provide the list. No intro or outro sentences.

Transcript:
{transcript}
"""
    response = model.generate_content(prompt)
    return response.text.strip()


# 3. Quiz (with Turkish output in JSON)
def generate_quiz(summary):
    prompt = f"""
You are an assistant that creates quiz questions based on a Turkish summary.

Instructions:
- Create 3 multiple choice questions in Turkish.
- Return them **strictly** in the following JSON format:

[
  {{
    "question": "Soru metni",
    "options": {{
      "A": "Seçenek A",
      "B": "Seçenek B",
      "C": "Seçenek C",
      "D": "Seçenek D"
    }},
    "correct_answer": "A",
    "explanation": "Doğru cevabın açıklaması"
  }},
  ...
]

Only return valid JSON. No greetings or extra text.

Summary:
{summary}
"""
    response = model.generate_content(prompt)
    text = response.text.strip()
    match = re.search(r'(\[\s*{.*}\s*\])', text, re.DOTALL)
    if match:
        json_text = match.group(1)
    else:
        json_text = text
    try:
        return json.loads(json_text)
    except Exception as e:
        print("Quiz formatı çözümlenemedi:", e)
        return {"error": "Quiz JSON formatı hatalı", "raw": response.text}


# 4. Lecture Notes
def generate_lecture_notes(transcript):
    prompt = f"""
You are a teaching assistant.

Instructions:
- Summarize the transcript in the form of Turkish lecture notes.
- Use this structure:

📌 Başlık  
- Açıklayıcı kısa cümle  
- Bullet list of key points

Do not include anything else.

Transcript:
{transcript}
"""
    response = model.generate_content(prompt)
    return response.text.strip()


# 5. Improve Summary with Feedback
def improve_summary(summary, feedback_type):
    prompt = f"""
You are an assistant that improves Turkish summaries based on user feedback.

Instructions:
- Rewrite the given summary based on the feedback.
- Keep it in Turkish.
- Only return the new summary text.

Original Summary:
{summary}

Feedback Type: {feedback_type}
"""
    response = model.generate_content(prompt)
    return response.text.strip()
