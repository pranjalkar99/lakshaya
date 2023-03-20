from youtube_transcript_api import YouTubeTranscriptApi

text_s=""
def get_transcript_v3(video_id):
    text_s=""
    srt = YouTubeTranscriptApi.get_transcript(video_id)
    for ele in srt:
        text_s+=ele['text']+" "
    return text_s