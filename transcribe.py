from youtube_transcript_api import YouTubeTranscriptApi
import re 

class GetVideo:
    @staticmethod
    def Id(link):
        """Extracts the video ID from a YouTube video link."""
        if "youtube.com" in link:
            pattern = r'youtube\.com/watch\?v=([a-zA-Z0-9_-]+)'
            match = re.search(pattern, link)
            if match:
                return match.group(1)
            else:
                return None
        elif "youtu.be" in link:
            pattern = r"youtu\.be/([a-zA-Z0-9_-]+)"
            match = re.search(pattern, link)
            if match:
                return match.group(1)
            else:
                return None
        else:
            return None

    @staticmethod
    def transcript(link):
        """Gets the transcript of a YouTube video."""
        video_id = GetVideo.Id(link)
        try:
            ytt_api = YouTubeTranscriptApi()
            # Specify language codes, e.g., try Turkish first, then English
            transcript_snippets = ytt_api.fetch(video_id, languages=['tr', 'en'])
            final_transcript = " ".join(snippet.text for snippet in transcript_snippets)
            return final_transcript
        except Exception as e:
            print(e)

if __name__ == "__main__":
    video_url = input("YouTube video linkini girin: ")
    transcript = GetVideo.transcript(video_url)
    print(transcript)
    
