import os
import youtube_dl
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# YouTube API Ayarları
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'

# IBM Watson Ayarları
IBM_API_KEY = 'YOUR_IBM_API_KEY'
IBM_URL = 'YOUR_SERVICE_URL'

# YouTube API'sini başlat
youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=YOUTUBE_API_KEY)

# IBM Watson Başlatma
authenticator = IAMAuthenticator(IBM_API_KEY)
speech_to_text = SpeechToTextV1(authenticator=authenticator)
speech_to_text.set_service_url(IBM_URL)

def get_channel_videos(channel_id, max_results=10):
    search_response = youtube.search().list(channelId=channel_id, part="id,snippet", maxResults=max_results).execute()
    return [{'title': item['snippet']['title'], 'id': item['id']['videoId']} for item in search_response.get("items", [])]

def download_video(video_id):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': f'{video_id}.wav',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'http://www.youtube.com/watch?v={video_id}'])

def convert_speech_to_text(filename):
    with open(filename, 'rb') as audio_file:
        result = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/wav',
            model='tr-TR_NarrowbandModel',
        ).get_result()
    transcripts = [res['alternatives'][0]['transcript'] for res in result['results']]
    return " ".join(transcripts)

def main(channel_id):
    videos = get_channel_videos(channel_id)
    with open("output.txt", "w", encoding="utf-8") as outfile:
        for video in videos:
            print(f"Processing {video['title']} ...")
            download_video(video['id'])
            transcript = convert_speech_to_text(f"{video['id']}.wav")
            outfile.write(f"Title: {video['title']}\n")
            outfile.write(transcript + "\n\n")
            os.remove(f"{video['id']}.wav")

if __name__ == "__main__":
    CHANNEL_ID = "YOUR_CHANNEL_ID"
    main(CHANNEL_ID)
