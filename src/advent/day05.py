from dataclasses import dataclass

__all__ = ["part1", "part2"]


@dataclass
class RangeMap:
    destination_start: int
    source_start: int
    range_length: int

    @classmethod
    def from_str(cls, s: str) -> "RangeMap":
        parts = [int(x) for x in s.strip().split()]
        return cls(parts[0], parts[1], parts[2])

    def convert(self, x: int) -> int:
        if self.source_start <= x < self.source_start + self.range_length:
            return x + (self.destination_start - self.source_start)
        return x


@dataclass
class EntityMap:
    source: str
    destination: str
    ranges: list[RangeMap]

    @classmethod
    def from_str(cls, s: str) -> "EntityMap":
        header, *range_lines = s.strip().splitlines()
        source, destination = header.split()[0].split("-to-")
        ranges = [RangeMap.from_str(x) for x in range_lines]
        return cls(source, destination, ranges)

    def convert(self, x: int) -> int:
        for r in self.ranges:
            if (result := r.convert(x)) != x:
                return result
        return x

def read_seeds(s: str) -> list[int]:
    return [int(x) for x in s.strip().split(": ")[-1].split()]

def get_min_location(seeds: list[int], maps: list[EntityMap]) -> int:
    cur = seeds
    for m in maps: # Big assumption that these are linear and in the right order
        cur = [m.convert(x) for x in cur]
    return min(cur)


def part1(inputs: str) -> int:
    seed_line, *map_strings = inputs.split("\n\n")
    seeds = read_seeds(seed_line)
    maps = [EntityMap.from_str(x) for x in map_strings]
    return get_min_location(seeds, maps)

def part2(inputs: str) -> int:
    seed_line, *map_strings = inputs.split("\n\n")
    seeds_repr = read_seeds(seed_line)
    seeds: list[int] = []
    for i in range(0, len(seeds_repr), 2):
        # wildly inefficient to check all these; will not work
        seeds += list(range(seeds_repr[i], seeds_repr[i] + seeds_repr[i+1]))
    maps = [EntityMap.from_str(x) for x in map_strings]
    return get_min_location(seeds, maps)
