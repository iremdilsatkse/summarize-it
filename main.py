# main.py
from fastapi import FastAPI, HTTPException, Request
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
    transcript = GetVideo.transcript(data.url)
    if not transcript:
        raise HTTPException(status_code=404, detail="Transcript not found")

    summary = summarize_text(transcript)
    return {"summary": summary}


@app.post("/highlights")
def highlights(data: VideoRequest):
    transcript = GetVideo.transcript(data.url)
    if not transcript:
        raise HTTPException(status_code=404, detail="Transcript not found")

    highlights = generate_highlights(transcript)
    return {"highlights": highlights}


@app.post("/quiz")
def quiz(data: VideoRequest):
    transcript = GetVideo.transcript(data.url)
    if not transcript:
        raise HTTPException(status_code=404, detail="Transcript not found")

    summary = summarize_text(transcript)
    quiz_data = generate_quiz(summary)

    # Eğer JSON parse edilememişse (hata varsa)
    if isinstance(quiz_data, dict) and "error" in quiz_data:
        raise HTTPException(status_code=500, detail="Quiz formatı hatalı: " + quiz_data["error"])

    return {"quiz": quiz_data}



@app.post("/lecture_notes")
def lecture_notes(data: VideoRequest):
    transcript = GetVideo.transcript(data.url)
    if not transcript:
        raise HTTPException(status_code=404, detail="Transcript not found")

    notes = generate_lecture_notes(transcript)
    return {"lecture_notes": notes}

@app.post("/improve_summary")
def improve(data: FeedbackRequest):
    improved = improve_summary(data.summary, data.feedback_type)
    return {"improved_summary": improved}

@app.get("/")
def root():
    return {"message": "API çalışıyor. Belgeler için /docs adresine gidin."}

# Lokal test için:
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
