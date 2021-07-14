"""Functions to update a single video description on YouTube."""

import difflib
import sys


def confirm_diff(old: str, new: str) -> bool:
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< OLD")
    print(old)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> NEW")
    print(new)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< DIFF")
    differ = difflib.unified_diff(old.splitlines(keepends=True), new.splitlines(keepends=True))
    sys.stdout.writelines(differ)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> DONE")
    while True:
        decision = input("Does this look correct [Y/n]? ")
        decision = decision.lower()
        if decision == '' or 'y' in decision:
            return True
        elif 'n' in decision:
            return False
        print("Invalid input, try again")


def update_description_on_youtube(youtube, video_id, new_description):
    if '<' in new_description or '>' in new_description:
        raise ValueError('new_description cannot contain < or >')

    # see https://developers.google.com/youtube/v3/docs/videos/list
    videos_list_response = youtube.videos().list(
        id=video_id,
        part='snippet'
    ).execute()

    if not videos_list_response['items']:
        raise KeyError(f'Video {video_id} was not found.')

    # Since the request specified a video ID, the response only contains one
    # video resource. This code extracts the snippet from that resource.
    videos_list_snippet = videos_list_response['items'][0]['snippet']

    if videos_list_snippet['description'] == new_description:
        print(f'Video {video_id}: new description and old description are the same, skipping...')
        return

    if not confirm_diff(old=videos_list_snippet['description'], new=new_description):
        print('diff rejected, aborting program...')
        sys.exit(0)

    # user has confirmed the new version looks good, go ahead
    videos_list_snippet['description'] = new_description

    # it seems like a bug in the youtube api that this needs to be done
    # a downloaded video may have no tags,
    # but omitting tags during upload results in 400 error
    if 'tags' not in videos_list_snippet:
        videos_list_snippet['tags'] = []

    # see https://developers.google.com/youtube/v3/docs/videos/update
    videos_update_response = youtube.videos().update(
        part='snippet',
        body=dict(
            snippet=videos_list_snippet,
            id=video_id
        )).execute()

    if videos_update_response['snippet']['description'] != new_description:
        raise RuntimeError('update failed')
