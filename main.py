"""
main.py

Bu dosya, tüm modülleri bir araya getirerek bir FastAPI REST sunucusu kurar.

API uç noktaları:
- /summarize → Başlık ve özet üretir
- /highlights → 5 önemli anı listeler
- /quiz → Quiz üretir (JSON)
- /lecture_notes → PDF olarak kaydetme için notları döner
- /improve_summary → Geri bildirimle özet geliştirir

Her uç nokta YouTube linki alır ve Gemini modelini kullanarak çıktılar döner.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transcribe import GetVideo
from summarize import (
    summarize_text,
    generate_highlights,
    generate_quiz,
    generate_lecture_notes,
    improve_summary
)
import uvicorn

app = FastAPI()

class VideoRequest(BaseModel):
    url: str

class FeedbackRequest(BaseModel):
    summary: str
    feedback_type: str


@app.post("/summarize")
def summarize_video(data: VideoRequest):
    """
    YouTube linkinden transkripti alır, başlık ve özet üretir.
    """
    transcript = GetVideo.transcript(data.url)

    if not transcript:
        raise HTTPException(status_code=404, detail="Transcript not found")

    title, summary = summarize_text(transcript)
    return {
        "title": title,
        "summary": summary
    }


@app.post("/highlights")
def highlights(data: VideoRequest):
    """
    Transkript üzerinden önemli anları döner.
    """
    transcript = GetVideo.transcript(data.url)
    if not transcript:
        raise HTTPException(status_code=404, detail="Transcript not found")

    highlights = generate_highlights(transcript)
    return {"highlights": highlights}


@app.post("/quiz")
def quiz(data: VideoRequest):
    """
    Özet üzerinden quiz soruları üretir.
    """
    transcript = GetVideo.transcript(data.url)
    if not transcript:
        raise HTTPException(status_code=404, detail="Transcript not found")

    title, summary = summarize_text(transcript)
    quiz_data = generate_quiz(summary)

    if isinstance(quiz_data, dict) and "error" in quiz_data:
        raise HTTPException(
            status_code=500, detail="Quiz formatı hatalı: " + quiz_data["error"])

    return {"quiz": quiz_data}


@app.post("/lecture_notes")
def lecture_notes(data: VideoRequest):
    """
    Transkript üzerinden ders notları üretir.
    """
    transcript = GetVideo.transcript(data.url)
    if not transcript:
        raise HTTPException(status_code=404, detail="Transcript not found")

    notes = generate_lecture_notes(transcript)
    return {"lecture_notes": notes}


@app.post("/improve_summary")
def improve(data: FeedbackRequest):
    """
    Kullanıcı geri bildirimine göre özeti geliştirir.
    """
    improved = improve_summary(data.summary, data.feedback_type)
    return {"improved_summary": improved}


@app.get("/")
def root():
    return {"message": "API çalışıyor. Belgeler için /docs adresine gidin."}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
