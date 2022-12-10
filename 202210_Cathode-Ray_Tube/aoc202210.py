# aoc_template.py

import pathlib
import sys
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=10)

def parse(puzzle_input):
    """Parse input."""
    return [i.split(' ') for i in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1."""    
    cycle = 1
    register_X = 1

    signal_strength = 0

    for instr in data:        
        if instr[0] == 'noop':
            cycle += 1
        elif instr[0] == 'addx':
            cycle += 1
            if cycle % 40 == 20:
                print(f"cycle {cycle}, signal strength {cycle * register_X}")
                signal_strength += cycle * register_X
            register_X += int(instr[1])
            cycle += 1
        else:
            raise ValueError(f"instruction is unknown: {instr[0]}")
        
        if cycle % 40 == 20:
            print(f"cycle {cycle}, signal strength {cycle * register_X}")
            signal_strength += cycle * register_X
    return signal_strength

def part2(data):
    """Solve part 2."""
    cycle = 0
    register_X = 1

    signal_strength = 0

    screen = ""

    for instr in data:        
        if instr[0] == 'noop':
            if cycle == register_X-1 or cycle == register_X or cycle == register_X+1:
                screen += '#'
            else:
                screen += '.'
            cycle += 1
            if cycle == 40:
                screen += '\n'
                cycle = 0
        elif instr[0] == 'addx':
            for i in range(2):
                if cycle == register_X-1 or cycle == register_X or cycle == register_X+1:
                    screen += '#'
                else:
                    screen += '.'
                cycle += 1
                if cycle == 40:
                    screen += '\n'
                    cycle = 0
                if i == 1:
                    register_X += int(instr[1])
        else:
            raise ValueError(f"instruction is unknown: {instr[0]}")
    return screen

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
    