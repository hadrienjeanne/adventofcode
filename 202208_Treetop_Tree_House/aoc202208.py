# aoc_template.py

import pathlib
import sys
from aocd.models import Puzzle
# from anytree import Node, RenderTree
from treelib import Node, Tree

puzzle = Puzzle(year=2022, day=8)

def parse(puzzle_input):
    """Parse input."""
    return [[c for c in i] for i in puzzle_input.split()]

def is_visible(forest, row, col):
    """Returns true if the tree in colomn col and row row is visible from outside."""    
    tree = forest[row][col]
    visible_top = True
    visible_down = True
    visible_left = True
    visible_right = True
    # check top
    for i in range(row):
        if forest[i][col] >= tree:            
            visible_top = False
    # check down
    for i in range(row+1, len(forest), 1):
        if forest[i][col] >= tree:            
            visible_down = False
    # check left
    for i in range(col):
        if forest[row][i] >= tree:            
            visible_left = False
    # check right
    for i in range(col+1, len(forest[row]), 1):
        if forest[row][i] >= tree:            
            visible_right = False
    return visible_top or visible_down or visible_left or visible_right

def scenic_score(forest, row, col):
    """Returns the scenic score of the tree in row row and col col."""
    tree = forest[row][col]
    score_top = 0
    score_down = 0
    score_left = 0
    score_right = 0
    # check top
    for i in range(row-1, -1, -1):
        if forest[i][col] < tree:            
            score_top += 1
        else:
            score_top += 1
            break    
    # check down
    for i in range(row+1, len(forest), 1):
        if forest[i][col] < tree:            
            score_down += 1
        else:
            score_down += 1
            break
    # check left
    for i in range(col-1, -1, -1):
        if forest[row][i] < tree:            
            score_left += 1
        else:
            score_left += 1
            break
    # check right
    for i in range(col+1, len(forest[row]), 1):
        if forest[row][i] < tree:            
            score_right += 1
        else:
            score_right += 1
            break
    return score_top * score_down * score_left * score_right

def part1(data):
    """Solve part 1."""
    nb_visibles = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if is_visible(data, row, col):
                nb_visibles += 1
    return nb_visibles
    
def part2(data):
    """Solve part 2."""
    max_scenic_score = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if scenic_score(data, row, col) > max_scenic_score:
                max_scenic_score = scenic_score(data, row, col)
    return max_scenic_score
    

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