from app.models.blackjack_models import BlackjackTurn


def take_turn(blackjack_turn: BlackjackTurn) -> dict:
    """
    Received all data needed to decide what action to take, should return either "Stand" or "Hit".
    :param blackjack_turn:
    :return:
    """
    return {"action": "Stand"}