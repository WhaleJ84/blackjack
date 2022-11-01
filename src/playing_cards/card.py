from unicodedata import lookup


class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = self._validate_rank(rank)
        self.suit = self._validate_suit(suit)
        self.unicode = lookup(f"PLAYING CARD {self.spoken_value().upper()}")
        # Not an attribute of a card. Move elsewhere
        self._values = {
            "ace": [11, 1],
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "jack": 10,
            "queen": 10,
            "king": 10
        }

    def __repr__(self) -> str:
        return f"{self.unicode} {self.spoken_value()}"

    @staticmethod
    def _validate_rank(rank: str):
        rank = rank.lower()
        valid_ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
        if rank in valid_ranks:
            return rank
        raise ValueError()

    @staticmethod
    def _validate_suit(suit: str):
        suit = suit.lower()
        valid_suits = ["clubs", "diamonds", "hearts", "spades"]
        if suit in valid_suits:
            return suit
        raise ValueError()

    def spoken_value(self):
        spoken_ranks = {
            "ace": "ace",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine",
            "10": "ten",
            "jack": "jack",
            "queen": "queen",
            "king": "king"
        }
        return f"{spoken_ranks[self.rank].title()} of {self.suit.title()}"
