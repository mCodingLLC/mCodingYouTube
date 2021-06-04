"""
Wrapper around Google's OAuth2 authentication process
providing convenience functions to build service objects.
"""

from typing import Iterator

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def get_authenticated_service(client_secret_file: str, scopes: list[str],
                              api_service_name: str, api_version: str):
    flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
    credentials = flow.run_console()
    return build(api_service_name, api_version, credentials=credentials)


def get_authenticated_readonly_service(client_secret_file: str):
    scopes = ['https://www.googleapis.com/auth/youtube.readonly']
    api_service_name = 'youtube'
    api_version = 'v3'
    return get_authenticated_service(client_secret_file, scopes, api_service_name, api_version)


def get_authenticated_readwrite_service(client_secret_file: str):
    scopes = ['https://www.googleapis.com/auth/youtube']
    api_service_name = 'youtube'
    api_version = 'v3'
    return get_authenticated_service(client_secret_file, scopes, api_service_name, api_version)


def paginated_results(youtube_listable_resource, list_request, limit_requests=10) -> Iterator:
    remaining = -1 if limit_requests is None else limit_requests
    while list_request and remaining != 0:
        list_response = list_request.execute()
        yield list_response
        # see googleapiclient/discovery.py createNextMethod for *_next methods
        list_request = youtube_listable_resource.list_next(list_request, list_response)
        remaining -= 1
