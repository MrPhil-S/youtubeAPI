from googleapiclient.discovery import build
import credentials

api_key = credentials.APIKey

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
        part='statistics',
        forUsername='schafer5'
    )

response = request.execute()

print(response)