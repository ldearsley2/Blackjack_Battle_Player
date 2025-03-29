from pathlib import Path
from pydantic_settings import BaseSettings


class Environment(BaseSettings):
    controller_url: str
    game_url: str
    player_nickname: str

    class Config:
        env_file = Path(__file__).parent.parent / ".env"


class AppSettings:
    def __init__(self, env_settings: Environment):
        self._env_settings = env_settings
        self.controller_url = env_settings.controller_url
        self.game_url = env_settings.game_url
        self.player_nickname = env_settings.player_nickname


SETTINGS = AppSettings(Environment())
