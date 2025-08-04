import streamlit as st
from transcribe import GetVideo
from summarize import (
    summarize_text,
    generate_highlights,
    generate_quiz,
    generate_concept_map,
    generate_lecture_notes,
    improve_summary
)

st.set_page_config(page_title="YouTube Video Summarizer", layout="wide")
st.title("🎥 YouTube Video Summarizer with AI")

youtube_url = st.text_input("🔗 Enter YouTube video URL:")

if st.button("📄 Generate Summary"):
    if not youtube_url:
        st.warning("⚠️ Please enter a valid YouTube URL.")
    else:
        with st.spinner("⏳ Extracting transcript..."):
            transcript = GetVideo.transcript(youtube_url)

        if not transcript:
            st.error(
                "❌ Transcript could not be retrieved. Please check the video link or enable subtitles.")
        else:
            st.success("✅ Transcript retrieved successfully!")

            with st.spinner("✍️ Generating summary..."):
                summary = summarize_text(transcript)

            st.markdown("### 📄 Video Summary")
            st.write(summary)

            # 🔹 Highlights with Timestamps
            with st.spinner("🔍 Generating highlights..."):
                highlights = generate_highlights(transcript)
            st.markdown("### ⏱️ Key Highlights with Timestamps")
            st.write(highlights)

            # 🔹 Quiz Generation
            with st.spinner("🧠 Generating quiz questions..."):
                quiz = generate_quiz(summary)
            st.markdown("### 🎓 Quiz Based on Summary")
            st.write(quiz)

            # 🔹 Concept Map
            with st.spinner("📌 Extracting key concepts and relationships..."):
                concept_map = generate_concept_map(summary)
            st.markdown("### 🧠 Concept Map")
            st.write(concept_map)

            # 🔹 Lecture Note Format
            with st.spinner("📚 Creating lecture-style notes..."):
                notes = generate_lecture_notes(transcript)
            st.markdown("### 📚 Lecture Notes")
            st.write(notes)

            # 🔹 Feedback-driven Summary Enhancement
            st.markdown("### ✨ Summary Feedback")
            feedback_option = st.selectbox(
                "Would you like an improved version of the summary?",
                [
                    "No, it's good as is.",
                    "Yes – Make it shorter and simpler.",
                    "Yes – Make it longer and more detailed."
                ]
            )

            if feedback_option != "No, it's good as is.":
                if st.button("🔁 Generate Improved Summary"):
                    with st.spinner("⚙️ Creating enhanced summary..."):
                        improved = improve_summary(summary, feedback_option)
                    st.markdown("### 🔄 Improved Summary")
                    st.write(improved)

            st.success("🎉 All outputs generated successfully!")
