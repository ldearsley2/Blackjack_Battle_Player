from enum import Enum

from app.models.blackjack_models import BlackjackTurn
from app.play.score import get_total


class Result(Enum):
    HIT = "Hit"
    STAND = "Stand"


def play(b: BlackjackTurn) -> Result:
    hand: list[str] = b.current_hand
    possible_totals = get_total(hand)
    for total in possible_totals:
        if int(b.dealer_stop) < total <= int(b.player_max_hand):
            return Result.STAND

    return Result.HIT
