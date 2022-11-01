from src.playing_cards.card import Card
from src.playing_cards.deck import Deck
from test.test_playing_cards import PlayingCardsTestCase


class DeckTestCase(PlayingCardsTestCase):
    def setUp(self) -> None:
        self.card = Card("ace", "clubs")
