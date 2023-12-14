import pytest
from typing import Callable
from textwrap import dedent
from advent import day01, day02, day03, day04, day05

Exercise = Callable[[str], int]
PerLineExpect = list[tuple[str, int]]

@pytest.mark.parametrize(["exercise_fn", "lines"], [
    (day01.part1, [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ]),
    (day01.part2, [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ]),
    (day02.part1, [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 1),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 2),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 0),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 0),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 5),
    ]),
    (day02.part2, [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 48),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 12),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 1560),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 630),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 36),
    ]),
    (day04.part1, [
        ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", 8),
        ("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", 2),
        ("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", 2),
        ("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", 1),
        ("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", 0),
        ("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", 0),
    ]),
], ids=lambda x: f"{x.__module__}.{x.__name__}" if hasattr(x, "__module__") else "")
class TestLineSumExercises:
    def test_line_by_line(self, exercise_fn: Exercise, lines: PerLineExpect):
        for line, expected in lines:
            assert exercise_fn(line) == expected

    def test_sample(self, exercise_fn: Exercise, lines: PerLineExpect):
        inputs = "\n".join(x[0] for x in lines)
        expected = sum(x[1] for x in lines)
        assert exercise_fn(inputs) == expected


@pytest.mark.parametrize(["exercise_fn", "expected", "inputs"], [
    (day03.part1, 4361, """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
    """),
    (day03.part2, 467835, """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
    """),
    (day04.part2, 30, """
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    """),
    (day05.part1, 35, """
        seeds: 79 14 55 13

        seed-to-soil map:
        50 98 2
        52 50 48

        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15

        fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4

        water-to-light map:
        88 18 7
        18 25 70

        light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13

        temperature-to-humidity map:
        0 69 1
        1 0 69

        humidity-to-location map:
        60 56 37
        56 93 4
    """),
    (day05.part2, 46, """
        seeds: 79 14 55 13

        seed-to-soil map:
        50 98 2
        52 50 48

        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15

        fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4

        water-to-light map:
        88 18 7
        18 25 70

        light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13

        temperature-to-humidity map:
        0 69 1
        1 0 69

        humidity-to-location map:
        60 56 37
        56 93 4
    """),
], ids=lambda x: f"{x.__module__}.{x.__name__}" if hasattr(x, "__module__") else "")
class TestFullStringExercises:
    def test_sample(self, exercise_fn: Exercise, expected: int, inputs: str):
        assert exercise_fn(dedent(inputs).strip()) == expected
