from abc import ABC
from enum import Enum
from typing import Optional

from game_state import GameState


class Suit(Enum):
    SWORDS = 0
    STAVES = 1
    CUPS = 2
    COINS = 3


class SuitColor(Enum):
    RED = 0
    BLACK = 1


class MinorRank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Card(ABC):
    def overlaying_top(self, state: GameState) -> Optional["Card"]:
        raise NotImplementedError()  # TODO

    def overlaying_bottom(self, state: GameState) -> Optional["Card"]:
        raise NotImplementedError()  # TODO

    @property
    def overlaying_bottom(self) -> Optional["Card"]:
        raise NotImplementedError()


class MinorArcanaCard(Card):
    def __init__(self, rank: MinorRank, suit: Suit):
        """

        :param rank: Card rank, from Ace to King
        :param suit: Card suit (swords, staves, cups, coins)
        """
        self.rank = rank
        self.suit = suit


class MajorArcanaCard(Card):

    full_suite_range = range(0, 22)

    def __init__(self, rank: int):
        if rank not in MajorArcanaCard.full_suite_range:
            raise ValueError("Rank out of range")

        self.rank = rank
