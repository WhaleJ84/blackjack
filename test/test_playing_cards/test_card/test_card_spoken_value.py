from test.test_playing_cards.test_card import CardTestCase


class CardSpokenValueTestCase(CardTestCase):
    def test_ace_of_clubs_value(self):
        self.assertEqual(
            self.card.spoken_value(),
            "Ace of Clubs"
        )

    def test_two_of_clubs_value(self):
        self.card.rank = "2"
        self.assertEqual(
            self.card.spoken_value(),
            "Two of Clubs"
        )

    def test_three_of_clubs_value(self):
        self.card.rank = "3"
        self.assertEqual(
            self.card.spoken_value(),
            "Three of Clubs"
        )

    def test_four_of_clubs_value(self):
        self.card.rank = "4"
        self.assertEqual(
            self.card.spoken_value(),
            "Four of Clubs"
        )

    def test_five_of_clubs_value(self):
        self.card.rank = "5"
        self.assertEqual(
            self.card.spoken_value(),
            "Five of Clubs"
        )

    def test_six_of_clubs_value(self):
        self.card.rank = "6"
        self.assertEqual(
            self.card.spoken_value(),
            "Six of Clubs"
        )

    def test_seven_of_clubs_value(self):
        self.card.rank = "7"
        self.assertEqual(
            self.card.spoken_value(),
            "Seven of Clubs"
        )

    def test_eight_of_clubs_value(self):
        self.card.rank = "8"
        self.assertEqual(
            self.card.spoken_value(),
            "Eight of Clubs"
        )

    def test_nine_of_clubs_value(self):
        self.card.rank = "9"
        self.assertEqual(
            self.card.spoken_value(),
            "Nine of Clubs"
        )

    def test_ten_of_clubs_value(self):
        self.card.rank = "10"
        self.assertEqual(
            self.card.spoken_value(),
            "Ten of Clubs"
        )

    def test_jack_of_clubs_value(self):
        self.card.rank = "jack"
        self.assertEqual(
            self.card.spoken_value(),
            "Jack of Clubs"
        )

    def test_queen_of_clubs_value(self):
        self.card.rank = "queen"
        self.assertEqual(
            self.card.spoken_value(),
            "Queen of Clubs"
        )

    def test_king_of_clubs_value(self):
        self.card.rank = "king"
        self.assertEqual(
            self.card.spoken_value(),
            "King of Clubs"
        )
