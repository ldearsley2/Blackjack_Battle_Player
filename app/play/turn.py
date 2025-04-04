from app.models.blackjack_models import BlackjackTurn, TurnAction
from app.play.score import get_total


def play(b: BlackjackTurn) -> TurnAction:
    hand: list[str] = b.current_hand
    possible_totals = get_total(hand)
    for total in possible_totals:
        if int(b.dealer_stop) <= total <= int(b.player_max_hand):
            return TurnAction.STAND

    return TurnAction.HIT
