import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

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

    Example (for illustration purposes only):
        Setting the Stage: Briefly introduce the video's topic and context.
        Key Points:
            Point A: Describe the first crucial aspect with clarity and depth.
            Point B: Elaborate on a second significant point.
            (Continue listing and describing key points)
        Conclusions: Summarize the video's main takeaways, leaving readers with a clear understanding and potential interest in learning more.

    Additional Tips:
        Tailor the tone: Adjust your language to resonate with the video's intended audience and overall style.
        Weave in storytelling elements: Employ vivid descriptions and engaging transitions to make the summary more memorable.
        Proofread carefully: Ensure your final summary is free of grammatical errors and typos.

    By following these guidelines, you can effectively transform video transcripts into captivating and informative summaries, drawing in readers and conveying the video's essence effectively.
        
    Video Transcript:
    {text}
    """
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    from transcribe import GetVideo
    video_url = input("YouTube video linkini girin: ")
    transcript = GetVideo.transcript(video_url)
    if transcript:
        summary = summarize_text(transcript)
        print("\Özet:\n", summary)
    else:
        print("Transkript alınamadı.")