from random import shuffle

from playing_cards import Card


class Deck:
    def __init__(self, cards: list = None):
        if cards is None:
            cards = list()
        self.cards = cards

    def shuffle(self, times: int = 1):
        """
        Shuffles the deck a specified number of times.

        :param times: Number of times to shuffle the deck
        """
        for time in range(times):
            shuffle(self.cards)
        return self.cards

    def add_card(self, card: Card):
        """
        Adds a card into the deck.

        :param card: The card to add into the deck
        """
        self.cards.append(card)
        return self.cards

    def remove_card(self, position_in_deck: int):
        """
        Removes a card from the deck.

        :param position_in_deck: The position of the card in the deck to remove
        """
        self.cards.pop(position_in_deck)
        return self.cards

    def draw_card(self, position_in_deck: int):
        """
        Draws a card in the given position from the deck

        :param position_in_deck: The position of the card in the deck to draw
        """
        return self.cards[position_in_deck]

    def draw_cards(self, number_of_cards: int = 1):
        """
        Draws a given number of cards before removing them from the deck

        :param number_of_cards: Number of cards to draw from the deck
        """
        cards = list()
        for card in range(number_of_cards):
            cards.append(self.draw_card(card))
            self.remove_card(card)
        return cards
