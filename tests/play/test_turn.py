import unittest

from app.models.blackjack_models import BlackjackTurn
from app.play.turn import play, Result


class TestPlay(unittest.TestCase):

    def setUp(self):
        dealer_stop = "17"
        player_max_hand = "21"
        player_id = "123"
        current_hand = []
        dealer_hand = []
        played_cards = []
        deck_amount = "2"
        b = BlackjackTurn(
            player_id=player_id,
            player_max_hand=player_max_hand,
            dealer_stop=dealer_stop,
            dealer_hand=dealer_hand,
            current_hand=current_hand,
            played_cards=played_cards,
            deck_amount=deck_amount

        )
        self.b = b

    def test_hit(self):
        self.b.current_hand = ["AH", "3S"]
        actual = play(self.b)
        self.assertEqual(Result.HIT, actual)

    def test_stand(self):
        self.b.current_hand = ["AH", "6C", "AD"]
        actual = play(self.b)
        self.assertEqual(Result.STAND, actual)
