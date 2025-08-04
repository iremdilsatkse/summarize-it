import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

# 1. Temel özetleme


def summarize_text(text):
    prompt = f"""
    Your task: Condense a video transcript into a captivating and informative 250-word summary that highlights key points and engages viewers.

    IMPORTANT: Always write the summary in Turkish, even if the transcript is in another language.

    Guidelines:
        Focus on essential information: Prioritize the video's core messages, condensing them into point-wise sections.
        Maintain clarity and conciseness: Craft your summary using accessible language, ensuring it's easily understood by a broad audience.
        Capture the essence of the video: Go beyond mere listings. Integrate key insights and interesting aspects to create a narrative that draws readers in.
        Word count: Aim for a maximum of 250 words.

    Input:
        The provided video transcript will be your content source.

    Video Transcript:
    {text}
    """
    response = model.generate_content(prompt)
    return response.text


# 2. Zaman Kodlu Önemli Noktalar (Highlights)
def generate_highlights(transcript):
    prompt = f"""
    Aşağıdaki video transkriptini incele ve bu videonun en önemli 5 anını belirle. Her önemli an için zaman kodu ve kısa açıklama ver.

    Format:
    🔹 [00:MM:SS] Açıklama

    Transkript:
    {transcript}
    """
    response = model.generate_content(prompt)
    return response.text


# 3. Quiz Soru-Cevap Oluşturma
def generate_quiz(summary):
    prompt = f"""
    Aşağıdaki video özetine göre 3 çoktan seçmeli soru oluştur.
    Her soru için:
    - 1 doğru, 3 yanlış seçenek ver.
    - Doğru cevabı belirt.
    - Cevap için kısa açıklama yaz.

    Video Özeti:
    {summary}
    """
    response = model.generate_content(prompt)
    return response.text


# 4. Konu Haritası (Concept Map)
def generate_concept_map(summary):
    prompt = f"""
    Aşağıdaki video özetine göre kavramları ve ilişkilerini çıkar.
    - Kavramları madde madde sırala
    - Aralarındaki bağlantıyı açıkla

    Video Özeti:
    {summary}
    """
    response = model.generate_content(prompt)
    return response.text


# 5. Ders Notu Formatında Özet
def generate_lecture_notes(transcript):
    prompt = f"""
    Aşağıdaki video transkriptini, ders notu formatında özetle.
    Yapı: 📌 Başlıklar → kısa açıklamalar → maddeler.

    Transkript:
    {transcript}
    """
    response = model.generate_content(prompt)
    return response.text


# 6. Kullanıcı Geri Bildirimiyle Geliştirilmiş Özet
def improve_summary(summary, feedback_type):
    prompt = f"""
    Mevcut özet:
    {summary}

    Kullanıcı geri bildirimi: {feedback_type}

    Lütfen bu geri bildirime göre özetin yeni bir versiyonunu oluştur.
    """
    response = model.generate_content(prompt)
    return response.text


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
