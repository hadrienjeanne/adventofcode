"""test_aoc_template.py"""

import pathlib
import pytest
import aoc202214 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    """example 1"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example):
    """Test that input is parsed properly."""
    assert example == [[['498', '4'], ['498', '6'], ['496', '6']], \
    [['503', '4'], ['502', '4'], ['502', '9'], ['494', '9']]]

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example):
    """Test part 1 on example input."""
    assert aoc.part1(example) == 24

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 93
