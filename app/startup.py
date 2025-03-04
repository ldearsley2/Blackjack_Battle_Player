import requests


def start_up_connect(game_url: str, own_url: str):
    data = {"url": own_url}
    response = requests.post(url=f"{game_url}/connect",
                             json=data)