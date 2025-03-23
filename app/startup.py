import requests
import websockets

from app.player_state import PlayerState


# def start_up_connect(game_url: str, own_url: str, player_state: PlayerState):
#     data = {
#         "url": own_url,
#         "nickname": "Lucas"
#     }
#     response = requests.post(url=f"{game_url}/connect", json=data)
#
#     player_state.set_player_id(response.json()["player_id"])
#
#     print(f"Player id: {player_state.player_id}")


async def start_up_socket(url: str, player_state: PlayerState):
    """
    Connect to give URL's websocket
    :param url:
    :param player_state:
    :return:
    """
    async with websockets.connect(url) as websocket:
        message = "Hello Server"
        await websocket.send(message)
        print("sent message")

        response = await websocket.recv()
        print(response)
