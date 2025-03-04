from abc import ABC
from enum import Enum
from typing import Optional


class Suit(Enum):
    SWORDS = 0
    STAVES = 1
    CUPS = 2
    COINS = 3


class SuitColor(Enum):
    RED = 0
    BLACK = 1


class Card(ABC):
    @property
    def overlaying_top(self) -> Optional["Card"]:
        raise NotImplementedError()

    @property
    def overlaying_bottom(self) -> Optional["Card"]:
        raise NotImplementedError()


class MinorArcanaCard(Card):
    def __init__(self, rank: int, suit: Suit):
        """

        :param rank: Card rank, ranging from 1 to 13; `A` = 1, `J` = 11, `Q` = 12, `K` = 13
        :param suit: Card suit (swords, staves, cups, coins)
        """
        if rank not in range(1, 13):
            raise ValueError("Rank out of range")

        self.rank = rank
        self.suit = suit


class MajorArcanaCard(Card):
    def __init__(self, rank: int):
        if rank not in range(0, 21):
            raise ValueError("Rank out of range")

        self.rank = rank