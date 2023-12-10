import pytest
from textwrap import dedent
from advent import day01, day02

class TestDay01:
    class TestPart1:
        @pytest.mark.parametrize("line,expected", [
            ("1abc2", 12),
            ("pqr3stu8vwx", 38),
            ("a1b2c3d4e5f", 15),
            ("treb7uchet", 77),
        ])
        def test_line_by_line(self, line: str, expected: int):
            assert day01.part1(line) == expected

        def test_sample(self):
            inputs = dedent("""
                1abc2
                pqr3stu8vwx
                a1b2c3d4e5f
                treb7uchet
            """).strip()
            assert day01.part1(inputs) == 142

    class TestPart2:
        @pytest.mark.parametrize("line,expected", [
            ("two1nine", 29),
            ("eightwothree", 83),
            ("abcone2threexyz", 13),
            ("xtwone3four", 24),
            ("4nineeightseven2", 42),
            ("zoneight234", 14),
            ("7pqrstsixteen", 76),
        ])
        def test_line_by_line(self, line: str, expected: int):
            assert day01.part2(line) == expected

        def test_sample(self):
            inputs = dedent("""
                two1nine
                eightwothree
                abcone2threexyz
                xtwone3four
                4nineeightseven2
                zoneight234
                7pqrstsixteen
            """).strip()
            assert day01.part2(inputs) == 281

class TestDay02:
    class TestPart1:
        @pytest.mark.parametrize("line,expected", [
            ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 1),
            ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 2),
            ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 0),
            ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 0),
            ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 5),
        ])
        def test_line_by_line(self, line: str, expected: int):
            assert day02.part1(line) == expected

        def test_sample(self):
            inputs = dedent("""
                Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
                Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
                Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
                Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
                Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
            """)
            assert day02.part1(inputs) == 8

    class TestPart2:
        @pytest.mark.parametrize("line,expected", [
            ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 48),
            ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 12),
            ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 1560),
            ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 630),
            ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 36),
        ])
        def test_line_by_line(self, line: str, expected: int):
            assert day02.part2(line) == expected

        def test_sample(self):
            inputs = dedent("""
                Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
                Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
                Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
                Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
                Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
            """)
            assert day02.part2(inputs) == 2286
