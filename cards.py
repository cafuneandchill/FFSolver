from enum import Enum


class Suit(Enum):
    SPADES = 0
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3


class Card:
    def __init__(self, suit: Suit, rank: int):
        """

        :param suit: Card suit
        :param rank: Card rank; `A` = 1, `J` = 11, `Q` = 12, `K` = 13
        """
        self.suit = suit
        self.rank = rank
