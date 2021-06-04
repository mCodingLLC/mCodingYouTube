"""
Configures client secret file to be looked
up at runtime in non-public .env file.
"""

import dotenv


class Config:

    def __init__(self, client_secret_file: str):
        self.client_secret_file: str = client_secret_file


config: Config = Config(**dotenv.dotenv_values('.env'))
