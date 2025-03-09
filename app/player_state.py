class PlayerState:
    def __init__(self):
        self.player_id = ""
        self.status = ""

    def set_player_id(self, player_id: str):
        self.player_id = player_id

    def set_player_bust(self):
        self.status = "Bust"


PLAYER_STATE = PlayerState()
