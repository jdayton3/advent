import pytest
from typing import Callable
from advent import day01, day02

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
    ])
], ids=lambda x: f"{x.__module__}.{x.__name__}" if hasattr(x, "__module__") else "")
class TestLineSumExercises:
    def test_line_by_line(self, exercise_fn: Callable[[str], int], lines: list[tuple[str, int]]):
        for line, expected in lines:
            assert exercise_fn(line) == expected

    def test_sample(self, exercise_fn: Callable[[str], int], lines: list[tuple[str, int]]):
        inputs = "\n".join(x[0] for x in lines)
        expected = sum(x[1] for x in lines)
        assert exercise_fn(inputs) == expected
