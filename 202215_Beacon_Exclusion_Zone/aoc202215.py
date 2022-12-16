"""advent of code 2022 day 15"""

import pathlib
import sys
import re
from aocd.models import Puzzle
from dataclasses import dataclass, field
from functools import lru_cache, reduce
from typing import NamedTuple

# %%time
from shapely import LineString, union_all, Polygon, difference


puzzle = Puzzle(year=2022, day=15)

@lru_cache
def manhattan(point_a, point_b):
    """computes the manhattan distance between 2 points"""
    return sum(abs(ai - bi) for ai, bi in zip(point_a, point_b))

class Point(NamedTuple):
    """class point"""
    x: int
    y: int

@dataclass
class Sensor:
    """class sensor"""
    coords: Point
    beacon: Point
    distance: int = field(init=False)

    def __post_init__(self):
        self.distance = manhattan(self.coords, self.beacon)

def parse(puzzle_input_data):
    """Parse input."""
    regex_sensor = re.compile(r"(-?\d+)")
    sensors = []
    for line in puzzle_input_data.split('\n'):
        s_x, s_y, b_x, b_y = map(int, regex_sensor.findall(line))
        sensors.append(Sensor(Point(s_x, s_y), Point(b_x, b_y)))
    return sensors

def part1(sensors):
    """Solve part 1."""
    limit = 2_000_000
    lines = []
    for sensor in sensors:
        if (diff := abs(sensor.coords.y - limit)) <= sensor.distance:
            delta = abs(sensor.distance - diff)
            line = LineString(((sensor.coords.x - delta, 0), (sensor.coords.x + delta, 0)))
            lines.append(line)
    return int(union_all(lines).length)

def part2(sensors):
    """Solve part 2."""
    limit = 4_000_000
    area = Polygon(((0, 0), (0, limit), (limit, limit), (limit, 0)))
    zones = (
        Polygon((
            (sensor.coords.x + sensor.distance, sensor.coords.y),
            (sensor.coords.x, sensor.coords.y + sensor.distance),
            (sensor.coords.x - sensor.distance, sensor.coords.y),
            (sensor.coords.x, sensor.coords.y - sensor.distance),
        )) for sensor in sensors
    )
    beacon = reduce(difference, zones, area).centroid
    return int(beacon.x) * limit + int(beacon.y)

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
