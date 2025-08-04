import google.generativeai as genai
import os
from dotenv import load_dotenv

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
Aşağıdaki özet metnine göre 3 çoktan seçmeli soru üret. Her soru için:

- 1 doğru, 3 yanlış seçenek
- Doğru cevabı açıkça belirt
- Cevap için kısa bir açıklama yaz

Giriş cümleleri veya açıklayıcı ifadeler kullanma. Yalnızca soru ve cevap içeriğini üret.

Özet:
{summary}
"""
    response = model.generate_content(prompt)
    return response.text.strip()


# 4. Konu Haritası (Concept Map)
def generate_concept_map(summary):
    prompt = f"""
Aşağıdaki özet metnine göre kavramları ve ilişkilerini çıkar. Aşağıdaki gibi yap:

- Kavramları madde madde sırala
- Her kavramın altına diğer kavramlarla ilişkisini kısa cümlelerle açıkla
- Giriş cümlesi veya açıklama yazma

Özet:
{summary}
"""
    response = model.generate_content(prompt)
    return response.text.strip()


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
        print("\n🧠 Konu Haritası:\n", generate_concept_map(summary))
        print("\n📚 Ders Notları:\n", generate_lecture_notes(transcript))

        feedback = input(
            "\nGeliştirme isteğiniz: [daha kısa / daha uzun / sade / detaylı]: ")
        print("\n✨ Geliştirilmiş Özet:\n", improve_summary(summary, feedback))

    else:
        print("Transkript alınamadı.")
