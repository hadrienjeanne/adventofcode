# aoc_template.py

import pathlib
import sys
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=9)

class Rope:
    def __init__(self, size, ropesize) -> None:
        self.grid = ['.' * size] * size
        self.rope = []
        for i in range(ropesize):
            self.rope.append([size//2, size//2])

    def __str__(self) -> str:
        output = ""
        for row, line in enumerate(self.grid):
            for col, char in enumerate(line):
                rope_char = ""
                for i in range(len(self.rope)):
                    if col == self.rope[i][0] and row == len(self.grid) - self.rope[i][1] - 1:
                        if i == 0:
                            rope_char += 'H'
                        else:
                            rope_char += str(i)
                if len(rope_char) > 0:
                    output += rope_char[:1]
                else:
                    output += char
            output += '\n'
        return output
                
    def move_head(self, direction):
        """moves the head one step in the direction dir"""
        if direction== 'U':
            self.rope[0][1] += 1
        elif direction == 'D':
            self.rope[0][1] -= 1
        elif direction == 'L':
            self.rope[0][0] -= 1
        elif direction == 'R':
            self.rope[0][0] += 1

    def update_tail(self):
        """updates the rope position depending on the head position"""
        for i in range(1, len(self.rope), 1):                          
            delta_col = self.rope[i-1][0] - self.rope[i][0]
            delta_row = self.rope[i-1][1] - self.rope[i][1]

            if abs(delta_row) > 1 or abs(delta_col) > 1:
                    ## Taking this shorcut from a github user. It removes
                    ## a lot of boiler plate code about diagonals. Basically,
                    ##  this will return either +1 or -1 cuz. 0 division will
                    ## be performed by 1 instead
                    delta_row //= abs(delta_row or 1)
                    delta_col //= abs(delta_col or 1)

                    self.rope[i][0] = self.rope[i][0] + delta_col
                    self.rope[i][1] = self.rope[i][1] + delta_row
            if i == len(self.rope) - 1:
                self.mark_visited(self.rope[i][0], self.rope[i][1])    

    def mark_visited(self, col, row):
        """marks the position in the grid by a #"""
        new_str = self.grid[len(self.grid) - row - 1][0:col] + '#' + self.grid[len(self.grid) - row - 1][col+1:]
        self.grid[len(self.grid) - row - 1] = new_str

def parse(puzzle_input):
    """Parse input."""
    return [i.split(' ') for i in puzzle_input.split('\n')]

def part1(data):
    """Solve part 1."""    
    rope = Rope(1000, 2)
    for instr in data:
        for i in range(int(instr[1])):
            rope.move_head(instr[0])
            rope.update_tail()

    return sum([line.count('#') for line in rope.grid])

def part2(data):
    """Solve part 2."""
    rope = Rope(1000, 10)
    for instr in data:
        for i in range(int(instr[1])):
            rope.move_head(instr[0])
            rope.update_tail()
            
    return sum([line.count('#') for line in rope.grid])

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
    