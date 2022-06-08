from urllib import response
import credentials
import json
from googleapiclient.discovery import build

api_key = credentials.APIKey

service = build('youtube', 'v3', developerKey = api_key)

request = service.channels().list(part='statistics', forUsername='schafer5')

try:
    response = request.execute()
except HttpError as e:
    print('error responce code :{0}, reason : {1}'.format(e.status_code, e.error_details))

#print(response)
print(json.dumps(response, sort_keys=True, indent=4))

service.close()
#books_service = build('books', 'v1', developerKey='api_key')
