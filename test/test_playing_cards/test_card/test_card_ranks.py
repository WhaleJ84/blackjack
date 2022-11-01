from test.test_playing_cards.test_card import CardTestCase


class CardRanksTestCase(CardTestCase):
    def test_ace_rank(self):
        self.assertEqual(
            self.card._validate_rank("ace"),
            "ace"
        )

    def test_two_rank(self):
        self.assertEqual(
            self.card._validate_rank("2"),
            "2"
        )

    def test_three_rank(self):
        self.assertEqual(
            self.card._validate_rank("3"),
            "3"
        )

    def test_four_rank(self):
        self.assertEqual(
            self.card._validate_rank("4"),
            "4"
        )

    def test_five_rank(self):
        self.assertEqual(
            self.card._validate_rank("5"),
            "5"
        )

    def test_six_rank(self):
        self.assertEqual(
            self.card._validate_rank("6"),
            "6"
        )

    def test_seven_rank(self):
        self.assertEqual(
            self.card._validate_rank("7"),
            "7"
        )

    def test_eight_rank(self):
        self.assertEqual(
            self.card._validate_rank("8"),
            "8"
        )

    def test_nine_rank(self):
        self.assertEqual(
            self.card._validate_rank("9"),
            "9"
        )

    def test_ten_rank(self):
        self.assertEqual(
            self.card._validate_rank("10"),
            "10"
        )

    def test_jack_rank(self):
        self.assertEqual(
            self.card._validate_rank("jack"),
            "jack"
        )

    def test_queen_rank(self):
        self.assertEqual(
            self.card._validate_rank("queen"),
            "queen"
        )

    def test_king_rank(self):
        self.assertEqual(
            self.card._validate_rank("king"),
            "king"
        )

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            self.card._validate_rank("prince")
