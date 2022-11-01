from src.playing_cards.card import Card
from test.test_playing_cards import PlayingCardsTestCase


class CardTestCase(PlayingCardsTestCase):
    def setUp(self) -> None:
        self.card = Card("ace", "clubs")
