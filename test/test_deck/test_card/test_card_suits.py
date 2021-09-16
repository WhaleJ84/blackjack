from test.test_deck.test_card import CardTestCase


class CardSuitsTestCase(CardTestCase):
    def test_clubs_suit(self):
        self.assertEqual(
            self.card._validate_suit("clubs"),
            "clubs"
        )

    def test_diamonds_suit(self):
        self.assertEqual(
            self.card._validate_suit("diamonds"),
            "diamonds"
        )

    def test_hearts_suit(self):
        self.assertEqual(
            self.card._validate_suit("hearts"),
            "hearts"
        )

    def test_spades_suit(self):
        self.assertEqual(
            self.card._validate_suit("spades"),
            "spades"
        )

    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            self.card._validate_suit("emeralds")
