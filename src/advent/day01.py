__all__ = ["part1", "part2"]

words = [
    ("zero", 0),
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
]

def part1(inputs: str) -> int:
    result = 0
    for line in inputs.strip().split("\n"):
        nums = [int(c) for c in line if c.isnumeric()]
        result += nums[0] * 10 + nums[-1]
    return result

def part2(inputs: str) -> int:
    result = 0
    for line in inputs.strip().split("\n"):
        first = [first_occurrence_index(line, word, str(num)) for word, num in words]
        last = [max(line.rfind(word), line.rfind(str(num))) for word, num in words]
        result += argmin(first) * 10 + argmax(last)
    return result

def first_occurrence_index(line: str, word: str, digit: str) -> int:
    max_index = len(line)
    word_index = line.find(word)
    digit_index = line.find(digit)
    if word_index == -1:
        word_index = max_index
    if digit_index == -1:
        digit_index = max_index
    return min(word_index, digit_index)

def argmax(iterable: list[int]) -> int:
    return max(enumerate(iterable), key=lambda x: x[1])[0]

def argmin(iterable: list[int]) -> int:
    return min(enumerate(iterable), key=lambda x: x[1])[0]
