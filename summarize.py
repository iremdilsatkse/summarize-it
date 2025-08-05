import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

# 1. Temel özetleme
def summarize_text(text):
    prompt = f"""
Aşağıdaki video transkriptine göre, maksimum 250 kelimelik Türkçe bir özet oluştur. Yalnızca özet metni üret. Selamlama, açıklama veya sohbet dili kullanma.

Transkript:
{text}
"""
    response = model.generate_content(prompt)
    return response.text.strip()


# 2. Zaman Kodlu Önemli Noktalar (Highlights)
def generate_highlights(transcript):
    prompt = f"""
Aşağıdaki transkripti analiz et. En önemli 5 anı belirle. Her biri için zaman kodu ve kısa açıklama ver. Giriş cümlesi veya sohbet dili kullanma. Sadece çıktıyı aşağıdaki formatta ver:

[00:MM:SS] Açıklama

Transkript:
{transcript}
"""
    response = model.generate_content(prompt)
    return response.text.strip()


# 3. Quiz Soru-Cevap Oluşturma
def generate_quiz(summary):
    prompt = f"""
Aşağıdaki özet metnine göre 3 çoktan seçmeli soru üret. Her soru için aşağıdaki JSON formatını **yalnızca** kullan:

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
    "explanation": "Neden doğru olduğunu açıkla."
  }},
  ...
]

**UYARI: Sadece geçerli JSON döndür. Açıklama, giriş veya başka bir şey ekleme.**

Özet:
{summary}
"""
    response = model.generate_content(prompt)
    text = response.text.strip()
    # JSON array'i ayıkla
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


# 5. Ders Notu Formatında Özet
def generate_lecture_notes(transcript):
    prompt = f"""
Aşağıdaki video transkriptini ders notu formatında özetle. Format şu şekilde olsun:

📌 Başlık  
- Kısa açıklama  
- İlgili maddeler (bullet list)

Sadece içerik üret, açıklayıcı cümle veya selamlamalar ekleme.

Transkript:
{transcript}
"""
    response = model.generate_content(prompt)
    return response.text.strip()


# 6. Kullanıcı Geri Bildirimiyle Geliştirilmiş Özet
def improve_summary(summary, feedback_type):
    prompt = f"""
Aşağıdaki özeti, verilen geri bildirim doğrultusunda yeniden oluştur. Selamlama veya açıklayıcı metin kullanma. Sadece özet çıktısını ver.

Özgün Özet:
{summary}

Geri Bildirim Türü: {feedback_type}
"""
    response = model.generate_content(prompt)
    return response.text.strip()


# CLI test için:
if __name__ == "__main__":
    from transcribe import GetVideo
    video_url = input("YouTube video linkini girin: ")
    transcript = GetVideo.transcript(video_url)
    if transcript:
        summary = summarize_text(transcript)
        print("\n📄 Özet:\n", summary)

        print("\n⏱️ Önemli Noktalar:\n", generate_highlights(transcript))
        print("\n🎓 Quiz:\n", generate_quiz(summary))
        print("\n📚 Ders Notları:\n", generate_lecture_notes(transcript))

        feedback = input(
            "\nGeliştirme isteğiniz: [daha kısa / daha uzun / sade / detaylı]: ")
        print("\n✨ Geliştirilmiş Özet:\n", improve_summary(summary, feedback))

    else:
        print("Transkript alınamadı.")
