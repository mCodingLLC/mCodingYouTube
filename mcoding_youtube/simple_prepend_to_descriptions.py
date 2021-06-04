"""
Script to read downloaded description data
and prepend text to all descriptions.
"""

import glob
import json

from mcoding_youtube.app_config import config
from mcoding_youtube.update_description_on_youtube import update_description_on_youtube
from mcoding_youtube.youtube import get_authenticated_readwrite_service


def get_videos_from_json_files(files):
    videos = []
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            playlist_list_response = json.load(f)
            videos.extend(playlist_list_response['items'])
    return videos


def load_text_to_prepend(file) -> str:
    with open(file, encoding='utf-8') as f:
        return ''.join(f.readlines()).strip() + '\n\n'


def main():
    files = glob.glob('data/my_videos_page_*.json')
    videos = get_videos_from_json_files(files)
    print(f'loaded {len(videos)=}')

    videos = [v for v in videos if 'patreon' not in v['snippet']['description'].lower()]
    print(f'{len(videos)=} after skipping ones that already have patreon')

    # try one before going crazy, comment out when confident
    test_title = 'Dictionary Union (or/pipe operator) - New Feature in Python 3.9'
    videos = [v for v in videos if v['snippet']['title'] == test_title]
    assert len(videos) == 1
    print(f'going to use {videos[0]["snippet"]["title"]}')

    patreon_text = load_text_to_prepend('patreon_text.txt')

    new_descriptions = {
        v['snippet']['resourceId']['videoId']: patreon_text + v['snippet']['description']
        for v in videos
    }

    if input("Start update process (must type YES)? ") != "YES":
        return

    client_secret_file = config.client_secret_file
    youtube = get_authenticated_readwrite_service(client_secret_file)

    for video_id, new_description in new_descriptions.items():
        update_description_on_youtube(youtube, video_id, new_description)


if __name__ == '__main__':
    main()
