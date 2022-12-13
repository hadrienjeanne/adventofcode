# aoc_template.py

from copy import deepcopy
from dataclasses import dataclass
import math
import pathlib
import sys
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=12)

class Node:
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value    
        self.neighbors = set()

    def __str__(self) -> str:
        ouput = f"Node {self.name} | {self.value} -> [{self.neighbors}]\n"       
        return ouput

    def __repr__(self) -> str:
        ouput = f"Node {self.name} | {self.value} -> [{self.neighbors}]\n"       
        return ouput

def parse(puzzle_input):
    """Parse input."""
    data = [i for i in puzzle_input.split('\n')]
    hill = {}
    height = len(data)
    width = len(data[0])
    start = None
    target = None
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            nodename = i * width + j
            
            if c == 'S':
                start = nodename
                c = 'a'
            elif c == 'E':
                target = nodename
                c = 'z'
            
            hill[nodename] = Node(nodename, c)

            if i > 0:
                target_char = data[i-1][j]
                if target_char == 'E': target_char = 'z'
                elif target_char == 'S': target_char = 'a'
                if abs(ord(target_char) - ord(c)) < 2:
                    hill[nodename].neighbors.add(nodename - width)                           
            if i < height - 1:
                target_char = data[i+1][j]
                if target_char == 'E': target_char = 'z'
                elif target_char == 'S': target_char = 'a'
                if abs(ord(target_char) - ord(c)) < 2:
                    hill[nodename].neighbors.add(nodename + width)
            if j > 0:
                target_char = data[i][j-1]
                if target_char == 'E': target_char = 'z'
                elif target_char == 'S': target_char = 'a'
                if abs(ord(target_char) - ord(c)) < 2:
                    hill[nodename].neighbors.add(nodename - 1)                     
            if j < width - 1:
                target_char = data[i][j+1]
                if target_char == 'E': target_char = 'z'
                elif target_char == 'S': target_char = 'a'
                if abs(ord(target_char) - ord(c)) < 2:
                    hill[nodename].neighbors.add(nodename + 1)
    return hill, start, target

def shortest_path(graph, start, target):
    """ BFS shortest path """
    path_list = [[start]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {start}
    if start == target:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = list(graph[last_node].neighbors)
        # Search goal node
        if target in next_nodes:
            current_path.append(target)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []



def part1(data):
    """Solve part 1.""" 
    hill, start, target = data
    print(hill, start, target)
    path = shortest_path(hill, 1770, 3398)
    print(f"path: {path}")
    return len(path) - 1

# start 3260 end 3398

# 1770 -> 3398 (104)

def part2(data):
    """Solve part 2."""
    

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
    