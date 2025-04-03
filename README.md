# Blackjack_Battle_Player

A Blackjack game player to be deployed within Cloud Run. All turn logic should be put in app/logic.py


## Installation

Install blackjack battle with poetry

```bash
  poetry install
```
    
## Deployment

To deploy this project locally:

```bash
  poetry run dev
```

To deploy this project in Cloud Run:
- Expose port 5000

## Environment Variables

These environment variables need to be populated:

```
CONTROLLER_URL: "The URL for the cloud run blackjack battle controller"
GAME_URL: "The URL for the cloud run instance of this player"
PLAYER_NICKNAME: "The player nickname used throughout the game"
```