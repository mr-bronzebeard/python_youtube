import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

youtube = None
youtube_api_key = 'YOUR_API_KEY'

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_secret.json"


def get_token_json():
    global youtube

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    # credentials = flow.run_console()
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)


def my_channel():
    tmp = {}
    # get_token_json()
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        mine=True
    )
    response = request.execute()

    tmp['items'] = response['items']

    return tmp['items'][0]


def search(options):
    tmp = {}
    request = youtube.search().list(
        part="snippet",
        maxResults=10,
        q=options
    )
    response = request.execute()

    tmp['items'] = response['items']

    return response
    # return tmp['items'][0]


def get_rating_by_group_id_videos(str_id):
    request = youtube.videos().list(
        part="statistics, player",
        id=str_id
    )
    response = request.execute()
    return response


def main():
    tmp = {}
    get_token_json()
    # request = youtube.channels().list(
    #   part="snippet,contentDetails,statistics",
    #  mine=True
    # )
    # response = request.execute()

    # tmp['items'] = response['items']

    # print(tmp['items'][0]['snippet']['thumbnails']['medium']['url'])

    search("kuplinov")

    # print(data['items']['snippet']['title'])
    # print(response)


if __name__ == "__main__":
    main()
