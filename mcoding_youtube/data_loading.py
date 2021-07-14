import json


def get_videos_from_json_files(files):
    videos = []
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            playlist_list_response = json.load(f)
            videos.extend(playlist_list_response['items'])
    return videos
