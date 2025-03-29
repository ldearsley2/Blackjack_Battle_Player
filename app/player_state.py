from app.config import SETTINGS


class PlayerState:
    def __init__(self):
        self.nickname = SETTINGS.player_nickname
        self.player_id = ""

    def set_player_id(self, player_id: str):
        self.player_id = player_id


PLAYER_STATE = PlayerState()
