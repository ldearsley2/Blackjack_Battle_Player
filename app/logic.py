from app.models.blackjack_models import BlackjackTurn

"""
player_id - The ID of this blackjack player,
player_max_hand - The max hand value before being bust,
dealer_stop - The hand value when the dealer stops pulling cards,
dealer_hand - The current cards in the dealers hand,
current_hand - The current cards in the players hand,
played_cards - All previously played cards before shuffling,
deck_amount - The amount of decks used by the dealer
"""

example_blackjack_turn = {
    "player_id": "bob",
    "player_max_hand": "21",
    "dealer_stop": "17",
    "dealer_hand": ["AH"],
    "current_hand": ["7D", "2S"],
    "played_cards": ["7D", "AH", "2S"],
    "deck_amount": "2",
}


def take_turn(blackjack_turn: BlackjackTurn) -> dict:
    """
    Received all data needed to decide what action to take,
    should return either {"action": "Stand"} or {"action": "Hit"}.
    :param blackjack_turn:
    :return:
    """
    return {"action": "Stand"}
