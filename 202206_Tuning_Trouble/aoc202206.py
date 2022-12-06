# aoc_template.py

import pathlib
import sys
from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=6)

def parse(puzzle_input):
    """Parse input."""
    # return [line for line in puzzle_input.split()]
    return [c for c in puzzle_input]

def get_marker_start(data, marker_size):
    """returns the position of the first marker of size marker_size"""
    marker = set()

    for i in range(len(data)-marker_size):
        marker.clear()    
        marker.update(data[i:i+marker_size])
        if len(marker) == marker_size:
            return i + marker_size

def part1(data):
    """Solve part 1."""
    return get_marker_start(data, 4)
    
def part2(data):
    """Solve part 2."""
    return get_marker_start(data, 14)
    

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