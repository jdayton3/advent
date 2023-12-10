import re
from dataclasses import dataclass

__all__ = ["part1", "part2"]

@dataclass
class CubeSet:
    red: int
    green: int
    blue: int

    @classmethod
    def from_str(cls, text: str) -> "CubeSet":
        red = re.search(r"(\d+) red", text)
        green = re.search(r"(\d+) green", text)
        blue = re.search(r"(\d+) blue", text)
        n_red = int(red.group(1)) if red else 0
        n_green = int(green.group(1)) if green else 0
        n_blue = int(blue.group(1)) if blue else 0
        return cls(n_red, n_green, n_blue)

    @property
    def power(self) -> int:
        return self.red * self.green * self.blue


@dataclass
class Game:
    game_id: int
    draws: list[CubeSet]

    @classmethod
    def from_line(cls, line: str) -> "Game":
        game_id_str, draws_str = line.split(": ")
        game_id = int(game_id_str.split(" ")[-1])
        draws = [CubeSet.from_str(x) for x in draws_str.split("; ")]
        return cls(game_id, draws)

    def is_cubeset_possible(self, cs: CubeSet) -> bool:
        return all([
            cs.red >= x.red and cs.green >= x.green and cs.blue >= x.blue
            for x in self.draws
        ])

    @property
    def min_cubeset(self) -> CubeSet:
        red = max(x.red for x in self.draws)
        green = max(x.green for x in self.draws)
        blue = max(x.blue for x in self.draws)
        return CubeSet(red, green, blue)

def part1(inputs: str) -> int:
    result = 0
    cubeset = CubeSet(red=12, green=13, blue=14)
    for line in inputs.strip().split("\n"):
        game = Game.from_line(line)
        if game.is_cubeset_possible(cubeset):
            result += game.game_id
    return result

def part2(inputs: str) -> int:
    result = 0
    for line in inputs.strip().split("\n"):
        result += Game.from_line(line).min_cubeset.power
    return result
