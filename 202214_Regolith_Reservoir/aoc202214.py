"""advent of code 2022 day 14"""

from collections import defaultdict
import pathlib
import sys
from aocd.models import Puzzle


puzzle = Puzzle(year=2022, day=14)


def parse(puzzle_input_data):
    """Parse input."""
    output = [[l.strip().split(',') for l in pair.split('->')]\
         for pair in puzzle_input_data.split('\n')]
    return output

def add_rocks(cavern: dict, rocks: str) -> dict:
    """Add rocks (#) into the dictionary and return the modified dictionary"""

    first_rock = rocks[0]
    remaining_rocks = rocks[1:]

    cavern[(int(first_rock[0]), int(first_rock[1]))] = '#'
    base_rock = [int(first_rock[0]), int(first_rock[1])]

    for rock in remaining_rocks:
        current_rock = rock
        current_rock[0] = int(current_rock[0])
        current_rock[1] = int(current_rock[1])
        if current_rock[0] == base_rock[0]: # same x, going vertically
            if current_rock[1] > base_rock[1]: # check if going up or down
                for y_rock in range(base_rock[1], current_rock[1] + 1):
                    cavern[(current_rock[0], y_rock)] = '#'
            else:
                for y_rock in range(current_rock[1], base_rock[1] + 1):
                    cavern[(current_rock[0], y_rock)] = '#'
        elif current_rock[1] == base_rock[1]: # same y, going horizontally
            if current_rock[0] > base_rock[0]: # check if going left or right
                for x_rock in range(base_rock[0], current_rock[0] + 1):
                    cavern[(x_rock, current_rock[1])] = '#'
            else:
                for x_rock in range(current_rock[0], base_rock[0] + 1):
                    cavern[(x_rock, current_rock[1])] = '#'
        base_rock = [current_rock[0], current_rock[1]]
    return cavern

def find_lowest_rock(cavern: dict) -> int:
    """Return the y value of the lowest rock so we can tell if sand is flowing into abyss."""
    rock_coordinates = [key[1] for key in cavern]
    return max(rock_coordinates)

def sand_simulation(cavern: dict, lowest_rock_y: int) -> int:
    """Return number of units sand before further sand will fall into the abyss."""
    protected = True
    sand_tally = 0
    while protected:
        falling = True
        sand_coordinate = [500, 0]
        while falling:
            # nothing below
            if cavern[(sand_coordinate[0], sand_coordinate[1] + 1)] not in ["#", "o"]:
                sand_coordinate[1] += 1
                if sand_coordinate[1] > lowest_rock_y:  # infinite falling
                    return sand_tally
            # nothing diag left -> fall
            elif cavern[(sand_coordinate[0] - 1, sand_coordinate[1] + 1)] not in ["#", "o"]:
                sand_coordinate[1] += 1
                sand_coordinate[0] -= 1
                if sand_coordinate[1] > lowest_rock_y:  # infinite falling
                    return sand_tally
            # nothin diag right -> fall
            elif cavern[(sand_coordinate[0] + 1, sand_coordinate[1] + 1)] not in ["#", 'o']:
                sand_coordinate[1] += 1
                sand_coordinate[0] += 1
                if sand_coordinate[1] > lowest_rock_y:  # infinite falling
                    return sand_tally
            else:  # nowhere left to go
                cavern[(sand_coordinate[0], sand_coordinate[1])] = 'o'
                falling = False
                sand_tally += 1
    return sand_tally

def sand_simulation_2(cavern: dict, lowest_rock_y: int) -> int:
    """Return number of units sand before further sand will fall into the abyss."""
    protected = True
    sand_tally = 0
    part_two_floor = lowest_rock_y + 2

    while protected:
        falling = True
        sand_coordinate = [500, 0]
        while falling:
            # nothing below
            if cavern[(sand_coordinate[0], sand_coordinate[1] + 1)] not in ["#", "o"]:
                if (sand_coordinate[1] + 1) == part_two_floor:
                    cavern[(sand_coordinate[0], sand_coordinate[1])] = 'o'
                    falling = False
                    sand_tally += 1
                else:
                    sand_coordinate[1] += 1
            # nothing diag left -> fall
            elif cavern[(sand_coordinate[0] - 1, sand_coordinate[1] + 1)] not in ["#", "o"]:
                if (sand_coordinate[1] + 1) == part_two_floor:
                    cavern[(sand_coordinate[0], sand_coordinate[1])] = 'o'
                    falling = False
                    sand_tally += 1
                else:
                    sand_coordinate[1] += 1
                    sand_coordinate[0] -= 1
            # nothin diag right -> fall
            elif cavern[(sand_coordinate[0] + 1, sand_coordinate[1] + 1)] not in ["#", 'o']:
                if (sand_coordinate[1] + 1) == part_two_floor:
                    cavern[(sand_coordinate[0], sand_coordinate[1])] = 'o'
                    falling = False
                    sand_tally += 1
                else:
                    sand_coordinate[1] += 1
                    sand_coordinate[0] += 1
            else:  # nowhere left to go
                cavern[(sand_coordinate[0], sand_coordinate[1])] = 'o'
                falling = False
                sand_tally += 1
                if sand_coordinate == [500, 0]:
                    return sand_tally
    return sand_tally


def part1(data):
    """Solve part 1."""
    cavern = defaultdict(str)
    for seam in data:
        cavern = add_rocks(cavern, seam)
    print(cavern)
    lowest_rock = find_lowest_rock(cavern)
    print(f"lowest rock {lowest_rock}")
    sand_before_abyss = sand_simulation(cavern, lowest_rock)
    print(f"{sand_before_abyss} grains of sand fell before flowing into the abyss.")
    return sand_before_abyss


def part2(data):
    """Solve part 2."""
    cavern = defaultdict(str)
    for seam in data:
        cavern = add_rocks(cavern, seam)
    print(cavern)
    lowest_rock = find_lowest_rock(cavern)
    part_two_sand = sand_simulation_2(cavern, lowest_rock)
    print(f"{part_two_sand} grains of sand fell before plugging the source.")
    return part_two_sand

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
    