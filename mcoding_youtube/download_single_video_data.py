import json

from mcoding_youtube.app_config import config
from mcoding_youtube.youtube import get_authenticated_readonly_service


def dump_json_to_file(obj, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(obj, f)


def download_video_data(youtube, video_id, file):
    # see https://developers.google.com/youtube/v3/docs/videos/list
    videos_list_response = youtube.videos().list(
        id=video_id,
        part='snippet'
    ).execute()

    if not videos_list_response['items']:
        raise KeyError(f'Video {video_id} was not found.')

    dump_json_to_file(videos_list_response, file)


def main():
    client_secret_file = config.client_secret_file
    youtube = get_authenticated_readonly_service(client_secret_file)
    video_id = "zrVfY9SuO64"
    save_to = f'data/{video_id}.json'
    download_video_data(youtube, video_id, save_to)


if __name__ == '__main__':
    main()
