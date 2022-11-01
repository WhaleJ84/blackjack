from json import load

from playing_cards import Card, Deck


class Player:
    def __init__(self, name: str, dealer: bool = False):
        self.name = name
        self.is_dealer = dealer
        self.hand = list()
        self.score = 0
        self.action = ""

    def status(self):
        return f"{self.name}: {self.score} {self.hand}"


class Game:
    def __init__(self):
        self.deck = self._initialise_deck()
        self.players = [
            Player('Player'),
            Player('Dealer', True)
        ]
        self.max_score = 0
        self.active = True

    @staticmethod
    def _initialise_deck():
        with open('playing_cards/52_card.json') as file:
            structure = load(file)

        deck = Deck()
        for suit, ranks in structure.items():
            for rank in ranks:
                deck.add_card(Card(rank, suit))
        return deck

    def get_score(self, participant, cards: list):
        for card in cards:
            if card.rank == "ace":
                if participant.score + 11 > 21:
                    participant.score += 1
                else:
                    participant.score += 11
            else:
                participant.score += card._values[card.rank]
        if participant.score > self.max_score:
            self.max_score = participant.score
        if self.max_score > 21:
            self.active = False

    def draw_cards(self, participant):
        if len(participant.hand) == 0:
            cards_drawn = self.deck.draw_cards(2)
        else:
            cards_drawn = self.deck.draw_cards(1)
        participant.hand.extend(cards_drawn)
        self.get_score(participant, cards_drawn)

    def prompt_player(self, participant):
        if not participant.is_dealer:
            print(participant.status())
            participant.action = input("Raise or Hold? [R/h]: ").lower()
            if "r" in list(participant.action) or participant.action == "":
                participant.action = "raise"
                self.draw_cards(participant)
            else:
                participant.action = "hold"
        else:
            if participant.score <= 17:
                self.draw_cards(participant)
            else:
                if self.players[0].action == "hold":
                    self.active = False
                else:
                    participant.action = "hold"


if __name__ == '__main__':
    blackjack = Game()
    blackjack.deck.shuffle(3)
    for player in blackjack.players:
        blackjack.draw_cards(player)

    while blackjack.active:
        for player in blackjack.players:
            player.action = ""
            while player.action != "hold" and blackjack.active:
                blackjack.prompt_player(player)

    print("END GAME")
    for player in blackjack.players:
        print(player.status())


