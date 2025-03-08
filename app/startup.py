import requests

from app.player_state import PlayerState


def start_up_connect(game_url: str, own_url: str, player_state: PlayerState):
    data = {"url": own_url}
    response = requests.post(url=f"{game_url}/connect",
                             json=data)

    player_state.set_player_id(response.json()["player_id"])

    print(f"Player id: {player_state.player_id}")
