# aoc_template.py

import pathlib
import sys
from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=5)

def parse_stack(line):
    """parse the input stack lines."""
    stack = [line[i:i+4].strip('[] ') for i in range(0, len(line), 4)]
    return stack

def parse(puzzle_input):
    """Parse input."""
    # return [line.split(',') for line in puzzle_input.split()]
    stacks = []
    instructions = []
    stack_mode = True

    # creation of the stacks as lists
    nb_stacks = (len(puzzle_input.split("\n")[0]) + 1) // 4
    for i in range(nb_stacks):
        stacks.append([])

    for line in puzzle_input.split("\n"):
        if line == "":
            stack_mode = False
            next
        if stack_mode and line[1] != "1":
            for n, crate in enumerate(parse_stack(line)):
                if crate != "":
                    stacks[n].insert(0, crate)
        elif line != "":
            instructions.append(line)    
    return stacks, instructions[1:]

def part1(data):
    """Solve part 1."""
    stacks = data[0]
    instructions = data[1]

    print(stacks)

    for instr in instructions:
        instruction = instr.split()
        nb_to_move = int(instruction[1])
        source_stack = int(instruction[3])
        target_stack = int(instruction[5])
        for i in range(nb_to_move):
            crate = stacks[source_stack - 1].pop()
            stacks[target_stack - 1].append(crate)
    
    return "".join([stacks[i].pop() for i in range(len(stacks))])

def part2(data):
    """Solve part 2."""
    stacks = data[0]
    instructions = data[1]

    print(stacks)

    for instr in instructions:
        instruction = instr.split()
        nb_to_move = int(instruction[1])
        source_stack = int(instruction[3])
        target_stack = int(instruction[5])
        target_length = len(stacks[target_stack - 1])
        for i in range(nb_to_move):            
            crate = stacks[source_stack - 1].pop()
            stacks[target_stack - 1].insert(target_length, crate)
    
    return "".join([stacks[i].pop() for i in range(len(stacks))])


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)    
    solution1 = part1(data)
    data = parse(puzzle_input)    
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