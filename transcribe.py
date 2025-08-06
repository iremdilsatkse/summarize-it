from youtube_transcript_api import YouTubeTranscriptApi
import re


class GetVideo:
    @staticmethod
    def Id(link):
        if "youtube.com" in link:
            pattern = r'youtube\.com/watch\?v=([a-zA-Z0-9_-]+)'
            match = re.search(pattern, link)
            if match:
                return match.group(1)
        elif "youtu.be" in link:
            pattern = r"youtu\.be/([a-zA-Z0-9_-]+)"
            match = re.search(pattern, link)
            if match:
                return match.group(1)
        return None

    @staticmethod
    def transcript(link):
        video_id = GetVideo.Id(link)
        try:
            ytt_api = YouTubeTranscriptApi()
            transcript_snippets = ytt_api.fetch(
                video_id, languages=['tr', 'en'])
            final_transcript = " ".join(
                snippet.text for snippet in transcript_snippets)
            return final_transcript
        except Exception as e:
            print(f"Error getting transcript: {e}")
            return None


if __name__ == "__main__":
    video_url = input("YouTube video linkini girin: ")
    transcript = GetVideo.transcript(video_url)
    print(f"Transcript: {transcript}")
