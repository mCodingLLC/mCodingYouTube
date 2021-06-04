import json

from mcoding_youtube.app_config import config
from mcoding_youtube.youtube import paginated_results, get_authenticated_readonly_service


def dump_json_to_file(obj, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(obj, f)


def get_my_uploads_playlist_id(youtube):
    # see https://developers.google.com/youtube/v3/docs/channels/list
    channels_response = youtube.channels().list(
        mine=True,
        part='contentDetails'
    ).execute()

    for channel in channels_response['items']:
        return channel['contentDetails']['relatedPlaylists']['uploads']

    return None


def download_playlist_video_snippets(youtube, playlist_id, file_prefix):
    # see https://developers.google.com/youtube/v3/docs/playlistItems/list
    playlistitems_list_request = youtube.playlistItems().list(
        playlistId=playlist_id,
        part='snippet',
        maxResults=50
    )

    results = paginated_results(youtube.playlistItems(), playlistitems_list_request)
    for page_no, playlistitems_list_response in enumerate(results):
        dump_json_to_file(playlistitems_list_response, f'{file_prefix}{page_no}.json')


def main():
    client_secret_file = config.client_secret_file
    youtube = get_authenticated_readonly_service(client_secret_file)
    uploads_playlist_id = get_my_uploads_playlist_id(youtube)
    file_prefix = 'data/my_videos_page_'
    if uploads_playlist_id is not None:
        download_playlist_video_snippets(youtube, uploads_playlist_id, file_prefix)
    else:
        print('There is no uploaded videos playlist for this user.')


if __name__ == '__main__':
    main()
