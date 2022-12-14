# aoc_template.py

import functools
import math
import pathlib
import sys
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=13)


def parse(puzzle_input):
    """Parse input."""
    return [[eval(l) for l in pair.split('\n')] for pair in puzzle_input.split('\n\n')]

def sign(l, r):
    if l < r:
        return 1
    elif l == r:
        return 0
    else:
        return -1

def compare(left, right):
    if not isinstance(left, list):
        if not isinstance(right, list):
            return sign(left, right) # int / int
        return compare([left], right) # int / list
    if not isinstance(right, list):
        return compare(left, [right]) # list / int
    if len(left) == 0 and len(right) == 0:
        return 0 # empty lists
    if len(left) == 0:
        return 1 # left empty before right
    if len(right) == 0:
        return -1 # right empty before left
    # Compare each array element until one is greater than the other
    for i in range(min(len(left), len(right))):
        result = compare(left[i], right[i])
        if result != 0:
            return result
    return sign(len(left), len(right)) # unequal array length

def part1(data):
    """Solve part 1."""     
    sum = 0
    for i, pair in enumerate(data):
        print(compare(pair[0], pair[1]))
        if compare(pair[0], pair[1]) == 1:
            sum += i+1
    return sum


def part2(data):
    """Solve part 2."""
    new_list = [[[2]], [[6]]]
    for pair in data:
        new_list.append(pair[0])
        new_list.append(pair[1])
    sorted_list = sorted(new_list, key=functools.cmp_to_key(compare), reverse=True)
    return (sorted_list.index([[2]]) + 1) * (sorted_list.index([[6]]) + 1) 
    

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
    