# test_aoc_template.py

import pathlib
import pytest
import aoc202208 as aoc
from treelib import Node, Tree

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [['3', '0', '3', '7', '3'], ['2', '5', '5', '1', '2'], ['6', '5', '3', '3', '2'], ['3', '3', '5', '4', '9'], ['3', '5', '3', '9', '0']]

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 21

# @pytest.mark.skip(reason="Not implemented")
def test_part2_tree1(example1):
    """Test part 2 on example input."""
    assert aoc.scenic_score(example1, 1, 2) == 4

# @pytest.mark.skip(reason="Not implemented")
def test_part2_tree2(example1):
    """Test part 2 on example input."""
    assert aoc.scenic_score(example1, 3, 2) == 8


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 0
