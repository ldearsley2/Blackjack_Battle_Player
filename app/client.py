import asyncio
import json

import websockets
from websockets import ConnectionClosed

from app.player_state import PlayerState

player_state = PlayerState()

def blackjack_decision():
    return "stand"

async def websocket_client():
    async with websockets.connect("ws://127.0.0.1:5000/connect") as websocket:
        # Send initial message
        message = {
            "action": "connect",
            "player_nickname": "Lucas"
        }
        await websocket.send(json.dumps(message))

        try:
            while True:
                response = await websocket.recv()
                response_json = json.loads(response)

                if "action" in response_json:

                    if response_json["action"] == "connected":
                        player_state.set_player_id(player_id=response_json["player_id"])
                        print(f"Connected with player_id: {player_state.player_id}")

                    elif response_json["action"] == "turn":
                        choice = {"action": blackjack_decision()}
                        await websocket.send(json.dumps(choice))

                print(response)

        except ConnectionClosed:
            print("Websocket connection closed")

asyncio.run(websocket_client())