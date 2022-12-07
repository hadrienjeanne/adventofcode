# aoc_template.py

import pathlib
import sys
from aocd.models import Puzzle
# from anytree import Node, RenderTree
from treelib import Node, Tree

puzzle = Puzzle(year=2022, day=7)

def parse(puzzle_input):
    """Parse input."""

    tree = Tree()
    current_node = tree.create_node('/')

    cmds = [line.split() for line in puzzle_input.split('\n')]
    for cmd in cmds[1:]:
        if cmd[0].startswith('$'):
            if cmd[1] == 'cd':
                if cmd[2] != '..':
                    if tree.get_node(cmd[2]) == None:
                        current_node = tree.create_node(cmd[2], parent=current_node)
                else: # cd ..
                    current_node = tree.parent(current_node.identifier)
            else: # ls
                pass
        elif cmd[0] == "dir":
            pass
        else: # file
            file = tree.create_node(cmd[1], parent=current_node, data=int(cmd[0]))
    tree.show()
    return tree

def part1(tree):
    """Solve part 1."""    
    sizes = {}
    sum_of_small_sizes = 0
    paths = tree.paths_to_leaves()
    for path in paths:
        file = tree.get_node(path[len(path)-1])
        for node in path[:len(path)-1]:
            sizes[tree.get_node(node).identifier] = sizes.get(tree.get_node(node).identifier, 0) + file.data

    # print(sizes)

    for size in sizes.values():
        if size <= 100000:
            sum_of_small_sizes += size
    return sum_of_small_sizes
    
def part2(tree):
    """Solve part 2."""
    total_disk_space = 70000000
    needed_space = 30000000
    sizes = {}
    sum_of_small_sizes = 0
    paths = tree.paths_to_leaves()
    for path in paths:
        file = tree.get_node(path[len(path)-1])
        for node in path[:len(path)-1]:
            sizes[tree.get_node(node).identifier] = sizes.get(tree.get_node(node).identifier, 0) + file.data

    used_space = sizes[tree.root]
    print("used_space", used_space)
    unused_space = total_disk_space - used_space
    print("unused space", unused_space)
    space_to_find = needed_space - unused_space
    print("we need to find ", space_to_find)

    min_dir_size_to_delete = used_space
    for size in sizes.values():
        if size >= space_to_find and size <= min_dir_size_to_delete:
            min_dir_size_to_delete = size

    return min_dir_size_to_delete

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