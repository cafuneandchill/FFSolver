from cards import Card, MinorArcanaCard, MinorRank

type CardStack = list[Card]


class MinorFoundations:
    def __init__(self,
                 swords: CardStack,
                 staves: CardStack,
                 cups: CardStack,
                 coins: CardStack,
                 cover_card: Card = None):
        self.swords = swords
        self.staves = staves
        self.cups = cups
        self.coins = coins
        self.cover_card = cover_card

    @property
    def is_covered(self) -> bool:
        if self.cover_card:
            return True
        return False

    @property
    def is_complete(self) -> bool:
        if (self.swords[-1].rank == MinorRank.KING
                and self.staves[-1].rank == MinorRank.KING
                and self.cups[-1].rank == MinorRank.KING
                and self.coins[-1].rank == MinorRank.KING):
            return True


class MajorFoundations:
    def __init__(self,
                 left_stack: CardStack,
                 right_stack: CardStack):
        self.left_stack = left_stack
        self.right_stack = right_stack

    @property
    def is_complete(self) -> bool:
        both_stacks = self.left_stack + self.right_stack
        if len(both_stacks) == 22:
            return True
        return False


class GameState:
    def __init__(self,
                 minor_foundations: MinorFoundations,
                 major_foundations, tableau):
        pass  # TODO