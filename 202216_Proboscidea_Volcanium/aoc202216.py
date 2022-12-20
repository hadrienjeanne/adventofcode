"""advent of code 2022 day 15"""

import pathlib
import sys
from dataclasses import dataclass
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=16)

@dataclass
class Valve:
    """A Valve, with a flow rate and tunnels leading to other valves"""
    name: str
    flow_rate: int
    tunnels: tuple
    closed: bool

def parse(puzzle_input_data):
    """Parse input."""
    data = [i.split(' ') for i in puzzle_input_data.split('\n')]
    valves = {}
    for line in data:
        name = line[1]
        flow_rate = int(line[4].split('=')[1].strip(';'))
        tunnels = ''.join(line[9:]).split(',')
        valve = Valve(name, flow_rate, tunnels, closed=True)
        valves[name] = valve
    return valves

def part1(data):
    """Solve part 1."""
    print(data)
    valves_open = []
    pressure = 0
    for minute in range(1, 31):
        print(f"== Minute {minute} ==")
        if valves_open:
            print(f"Valve {valves_open} is open, releasing {pressure} pressure.")
        else:
            print("No valves are open.")
    return pressure

def part2(data):
    """Solve part 2."""
    return 0

def solve(puzzle_input_data):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input_data)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    # either input via a file given in argument or via aoc input plugin
    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            print(f"{path}:")
            puzzle_input = pathlib.Path(path).read_text(encoding='UTF-8').strip()
    else:
        puzzle_input = puzzle.input_data

    print(f"input: \n {puzzle_input[:20]}")
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
    
# %%
