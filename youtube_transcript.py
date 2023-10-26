from youtube_transcript_api import YouTubeTranscriptApi

def get_video_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([line['text'] for line in transcript_list])
        return transcript
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

video_url = input("Enter the YouTube video URL: ")

video_id = video_url.split("=")[-1]

transcript = get_video_transcript(video_id)

if transcript:
    with open('transcript.txt', 'w') as f:
        f.write(transcript)
    print("Transcript saved to transcript.txt")
else:
    print("Failed to retrieve the transcript.")
