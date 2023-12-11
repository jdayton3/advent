from dataclasses import dataclass

__all__ = ["part1", "part2"]


@dataclass
class Card:
    game_id: int
    winners: list[int]
    numbers: list[int]

    @classmethod
    def from_line(cls, line: str) -> "Card":
        game_id_str, all_nums_str = line.split(": ")
        game_id = int(game_id_str.split(" ")[-1])
        win_str, your_str = all_nums_str.split(" | ")
        winners = [int(x) for x in win_str.split()]
        numbers = [int(x) for x in your_str.split()]
        return cls(game_id, winners, numbers)

    @property
    def score(self) -> int:
        return int(2**(self.n_winners-1))

    @property
    def n_winners(self) -> int:
        win_set = set(self.winners)
        return sum(1 for x in self.numbers if x in win_set)

@dataclass
class CardDuplicator:
    cards: list[Card]

    @classmethod
    def from_str(cls, s: str) -> "CardDuplicator":
        return cls([Card.from_line(line) for line in s.strip().split("\n")])

    def score(self) -> int:
        n_cards = [1] * len(self.cards)
        winner_counts = [c.n_winners for c in self.cards]
        for i, n in enumerate(winner_counts):
            n_current = n_cards[i]
            for j in range(i+1, i+n+1):
                n_cards[j] += n_current
        return sum(n_cards)

def part1(inputs: str) -> int:
    result = 0
    for line in inputs.strip().split("\n"):
        result += Card.from_line(line).score
    return result

def part2(inputs: str) -> int:
    return CardDuplicator.from_str(inputs).score()
