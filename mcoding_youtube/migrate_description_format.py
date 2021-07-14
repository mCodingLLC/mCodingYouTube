"""
Update all live video descriptions from one format to another.
"""

import glob

from mcoding_youtube.app_config import config
from mcoding_youtube.data_loading import get_videos_from_json_files
from mcoding_youtube.update_description_on_youtube import update_description_on_youtube
from mcoding_youtube.youtube import get_authenticated_readwrite_service
from mcoding_youtube.description_parsing import description_to_parts, parts_to_description_v2


def main():
    files = glob.glob('data/my_videos_page_*.json')
    videos = get_videos_from_json_files(files)
    print(f'loaded {len(videos)=}')

    def updated_description(s: str) -> str:
        return parts_to_description_v2(description_to_parts(s))

    new_descriptions = {
        v['snippet']['resourceId']['videoId']: updated_description(v['snippet']['description'])
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
