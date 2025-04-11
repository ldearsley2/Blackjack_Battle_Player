from enum import Enum

from pydantic import BaseModel


class BlackjackTurn(BaseModel):
    player_id: str
    player_max_hand: str
    dealer_stop: str
    dealer_hand: list[str]
    current_hand: list[str]
    played_cards: list[str]
    deck_amount: str


class BlackjackBet(BaseModel):
    player_id: str
    current_points: int


class ManualConnect(BaseModel):
    player_id: str


class TurnAction(Enum):
    HIT = "Hit"
    STAND = "Stand"
