from src.deck.card import Card
from test.test_deck import DeckTestCase


class CardTestCase(DeckTestCase):
    def setUp(self) -> None:
        self.card = Card("ace", "clubs")
