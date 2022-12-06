# aoc_template.py

import pathlib
import sys
from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=3)


def get_priority(letter):
    """returns the item priority."""
    if letter.islower():
        return ord(letter) - ord('a') + 1
    elif letter.isupper():
        return ord(letter) - ord('A') + 27
    else:
        return -1

def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split()]

def part1(data):
    """Solve part 1."""
    priorities = 0
    for rucksack in data:
        compartment_one = set(rucksack[:len(rucksack) // 2])
        compartment_two = set(rucksack[len(rucksack) // 2:])
        for item in compartment_one:
            if item in compartment_two:
                priorities += get_priority(item)
    return priorities
    

def part2(data):
    """Solve part 2."""
    groups = [data[i : i+3] for i in range(0, len(data), 3)]
    priorities = 0

    for group in groups:
        rucksack_one = set(group[0])
        rucksack_two = set(group[1])
        rucksack_three = set(group[2])
        intersection = rucksack_one & rucksack_two & rucksack_three
        priorities += get_priority(intersection.pop())
    return priorities

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)    
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    """Main function."""
    # either input via a file given in argument or via aoc input plugin    
    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            print(f"{path}:")
            puzzle_input = pathlib.Path(path).read_text().strip()
    else:
        puzzle_input = puzzle.input_data

    print(f"input: \n {puzzle_input[:50]}")
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))