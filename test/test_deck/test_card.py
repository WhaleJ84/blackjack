from unittest import TestCase

from src.deck.card import Card


class CardTestCase(TestCase):
    def test_validate_suit_returns_suit_on_lowercase_valid_input(self):
        self.assertEqual(
            Card("ace", "clubs").suit,
            "clubs"
        )

    def test_validate_suit_returns_suit_on_uppercase_valid_input(self):
        self.assertEqual(
            Card("ace", "Clubs").suit,
            "clubs"
        )

    def test_validate_suit_raises_exception_on_invalid_suit(self):
        with self.assertRaises(ValueError):
            Card("ace", "emeralds")

    def test_validate_rank_returns_rank_on_lowercase_valid_string(self):
        self.assertEqual(
            Card("ace", "clubs").rank,
            "ace"
        )

    def test_validate_rank_returns_rank_on_uppercase_valid_string(self):
        self.assertEqual(
            Card("Ace", "clubs").rank,
            "ace"
        )

    def test_validate_rank_returns_rank_on_valid_integer(self):
        self.assertEqual(
            Card("10", "clubs").rank,
            "10"
        )

    def test_validate_rank_raises_exception_on_invalid_rank(self):
        with self.assertRaises(ValueError):
            Card("prince", "clubs")

    def test_card_unicode_returns_valid_unicode(self):
        self.assertEqual(
            Card("ace", "clubs").unicode,
            "🃑"
        )

    def test_info_returns_readable_context(self):
        self.assertEqual(
            Card("ace", "clubs").info(),
            "Ace of Clubs"
        )
