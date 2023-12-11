from dataclasses import dataclass, field
from enum import Enum, auto

__all__ = ["part1", "part2"]

@dataclass
class Region:
    """start-inclusive, end-exclusive ranges"""
    row: tuple[int, int]
    col: tuple[int, int]

    def overlaps(self, other: "Region") -> bool:
        return (
            set(range(*self.row)).intersection(set(range(*other.row))) != set()
            and set(range(*self.col)).intersection(set(range(*other.col))) != set()
        )

    def overlaps_any(self, others: "list[Region]") -> bool:
        return any(self.overlaps(x) for x in others)

@dataclass
class NumberLocation:
    number: int
    region: Region

@dataclass
class SymbolLocation:
    symbol: str
    region: Region

    @classmethod
    def at_coords(cls, symbol: str, row: int, col: int) -> "SymbolLocation":
        return cls(symbol, Region((row-1, row+2), (col-1, col+2)))


class CharType(Enum):
    DIGIT = auto()
    ROW_END = auto()
    SYMBOL = auto()
    OTHER = auto()

    @classmethod
    def from_char(cls, c: str) -> "CharType":
        if c.isnumeric():
            return cls.DIGIT
        if c == "\n":
            return cls.ROW_END
        if c.isalpha() or c == "." or c.strip() == "":
            return cls.OTHER
        return cls.SYMBOL


@dataclass
class Gear:
    loc: SymbolLocation
    parts: tuple[NumberLocation, NumberLocation]

    @property
    def ratio(self) -> int:
        return self.parts[0].number * self.parts[1].number


@dataclass
class MatrixReadState:
    row: int = 0
    col: int = 0
    in_number: bool = False
    number: int = 0
    start_index: int = 0
    active_regions: list[Region] = field(default_factory=list)
    symbols: list[SymbolLocation] = field(default_factory=list)
    numbers: list[NumberLocation] = field(default_factory=list)

    def read_character(self, c: str):
        char_type = CharType.from_char(c)
        if char_type == CharType.DIGIT:
            if self.in_number:
                self.number *= 10
                self.number += int(c)
            else:
                self.number = int(c)
                self.start_index = self.col
                self.in_number = True
        else:
            if self.in_number:
                self.numbers.append(NumberLocation(
                    self.number,
                    Region((self.row, self.row+1), (self.start_index, self.col))
                ))
                self.in_number = False
                self.number = 0

        if char_type == CharType.SYMBOL:
            sym = SymbolLocation.at_coords(c, self.row, self.col)
            self.symbols.append(sym)
            self.active_regions.append(sym.region)

        if char_type == CharType.ROW_END:
            self.row += 1
            self.col = 0
        else:
            self.col += 1

    @property
    def active_numbers(self) -> list[NumberLocation]:
        return [x for x in self.numbers if x.region.overlaps_any(self.active_regions)]

    @property
    def gears(self) -> list[Gear]:
        result: list[Gear] = []
        potential_gears = [x for x in self.symbols if x.symbol == "*"]
        for symbol in potential_gears:
            overlaps = [x for x in self.numbers if symbol.region.overlaps(x.region)]
            if len(overlaps) == 2:
                result.append(Gear(symbol, (overlaps[0], overlaps[1])))
        return result

    @property
    def gear_ratio(self) -> int:
        return sum(gear.ratio for gear in self.gears)




def part1(inputs: str) -> int:
    state = MatrixReadState()
    for c in inputs.strip() + "\n":
        state.read_character(c)
    return sum(n.number for n in state.active_numbers)

def part2(inputs: str) -> int:
    state = MatrixReadState()
    for c in inputs.strip() + "\n":
        state.read_character(c)
    return state.gear_ratio
