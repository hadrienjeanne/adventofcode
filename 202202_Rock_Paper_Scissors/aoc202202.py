# aoc_template.py

import pathlib
import sys
from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=2)

def parse(puzzle_input):
    """Parse input."""
    # strategy_guide = []
    # for line in puzzle_input.split('\n'):
    #     strategy_guide.append(line.split())
    return [line.split() for line in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1."""
    score = 0
    for play in data:
        if play[0] == 'A':
            if play[1] == 'Y':
                score += 6 + 2
            elif play[1] == 'X':
                score += 3 + 1
            else:
                score += 3
        elif play[0] == 'B':
            if play[1] == 'Z':
                score += 6 + 3
            elif play[1] == 'Y':
                score += 3 + 2
            else:
                score += 1
        elif play[0] == 'C':
            if play[1] == 'X':
                score += 6 + 1
            elif play[1] == 'Z':
                score += 3 + 3
            else:
                score += 2
    return score

def part2(data):
    """Solve part 2."""
    score = 0
    for play in data:
        if play[1] == 'X': # lose
            if play[0] == 'A': # doit jouer Z
                score += 3
            elif play[0] == 'B': # doit jouer X
                score += 1
            elif play[0] == 'C': # doit jouer Y
                score += 2
        elif play[1] == 'Y': # tie
            if play[0] == 'A': # doit jouer X
                score += 3 + 1
            elif play[0] == 'B': # doit jouer Y
                score += 3 + 2
            elif play[0] == 'C': # doit jouer Z
                score += 3 + 3
        elif play[1] == 'Z': # win
            if play[0] == 'A': # doit jouer Y
                score += 6 + 2
            elif play[0] == 'B': # doit jouer Z
                score += 6 + 3
            elif play[0] == 'C': # doit jouer X
                score += 6 + 1
    return score

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

    print(f"input: \n {puzzle_input[:20]}")
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))