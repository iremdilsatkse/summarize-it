import streamlit as st
from transcribe import GetVideo
from summarize import summarize_text

st.title("YouTube Video Summarizer")

youtube_url = st.text_input("YouTube video linkini girin:")

if st.button("Özetle"):
    if not youtube_url:
        st.warning("Lütfen bir YouTube bağlantısı girin.")
    else:
        with st.spinner("Transkript alınıyor (YouTube)..."):
            transcript = GetVideo.transcript(youtube_url)
        if not transcript:
            st.error("Transkript alınamadı. Lütfen geçerli bir YouTube bağlantısı girin.")
        else:
            st.success("Transkript başarıyla alındı!")
            with st.spinner("Özet oluşturuluyor (Gemini)..."):
                summary = summarize_text(transcript)
            st.markdown("### Video Özeti")
            st.write(summary)