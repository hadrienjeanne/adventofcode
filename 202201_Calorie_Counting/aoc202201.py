# aoc_template.py

import pathlib
import sys
from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=1)

def parse(puzzle_input):
    """Parse input."""
    # cal_list = [int(line) for line in puzzle_input.split()]     
    cal_list = []
    cal_sum = 0    
    for line in puzzle_input.split("\n"):                
        if line == "":            
            cal_list.append(cal_sum)
            cal_sum = 0
        else:
            cal_sum += int(line)
    print(cal_list)
    return cal_list

def part1(data):
    """Solve part 1."""
    return max(data)


def part2(data):
    """Solve part 2."""
    return sum(sorted(data, reverse=True)[:3])

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

    # print(f"input:\n{puzzle_input[:50]}")
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))