import unittest

from app.play.score import get_score, get_total


class TestScore(unittest.TestCase):

    def test_number_card(self):
        self.assertEqual([7], get_score("7H"))
        self.assertEqual([10], get_score("10C"))

    def test_picture_card(self):
        self.assertEqual([10], get_score("KD"))
        self.assertEqual([10], get_score("QS"))

    def test_ace(self):
        self.assertEqual([1, 10], get_score("AH"))


class TestTotal(unittest.TestCase):

    def test_numbers_only(self):
        self.assertEqual([11], get_total(["7H", "4D"]))

    def test_numbers_and_pictures(self):
        self.assertEqual([17], get_total(["5H", "JS", "2C"]))

    def test_aces(self):
        self.assertEqual([4, 13], get_total(["AH", "3S"]))
        self.assertEqual([10, 19, 28], get_total(["6S", "AH", "2C", "AC"]))
        self.assertEqual([11, 20, 29, 38, 47], get_total(["AS", "AH", "2C", "AC", "5D", "AD"]))
