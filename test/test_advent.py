import pytest
from textwrap import dedent
from advent.day01 import part1, part2

class TestDay01:
    class TestPart1:
        @pytest.mark.parametrize("line,expected", [
            ("1abc2", 12),
            ("pqr3stu8vwx", 38),
            ("a1b2c3d4e5f", 15),
            ("treb7uchet", 77),
        ])
        def test_line_by_line(self, line: str, expected: int):
            assert part1(line) == expected

        def test_sample(self):
            inputs = dedent("""
                1abc2
                pqr3stu8vwx
                a1b2c3d4e5f
                treb7uchet
            """).strip()
            assert part1(inputs) == 142

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
            assert part2(line) == expected

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
            assert part2(inputs) == 281
