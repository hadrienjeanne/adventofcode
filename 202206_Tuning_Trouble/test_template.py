# test_aoc_template.py

import pathlib
import pytest
import aoc202206 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example5():
    puzzle_input = (PUZZLE_DIR / "example5.txt").read_text().strip()
    return aoc.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ['m', 'j', 'q', 'j', 'p', 'q', 'm', 'g', 'b', 'l', 'j', 's', 'p', 'h', 'd', 'z', 't', 'n', 'v', 'j', 'f', 'q', 'w', 'r', 'c', 'g', 's', 'm', 'l', 'b']

# @pytest.mark.skip(reason="Not implemented")
def test_parse_example2(example2):
    """Test that input is parsed properly."""
    assert example2 == ['b', 'v', 'w', 'b', 'j', 'p', 'l', 'b', 'g', 'v', 'b', 'h', 's', 'r', 'l', 'p', 'g', 'd', 'm', 'j', 'q', 'w', 'f', 't', 'v', 'n', 'c', 'z']

# @pytest.mark.skip(reason="Not implemented")
def test_parse_example3(example3):
    """Test that input is parsed properly."""
    assert example3 == ['n', 'p', 'p', 'd', 'v', 'j', 't', 'h', 'q', 'l', 'd', 'p', 'w', 'n', 'c', 'q', 's', 'z', 'v', 'f', 't', 'b', 'r', 'm', 'j', 'l', 'h', 'g']

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 7

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc.part1(example2) == 5

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc.part1(example3) == 6

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example4(example4):
    """Test part 1 on example input."""
    assert aoc.part1(example4) == 10

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example5(example5):
    """Test part 1 on example input."""
    assert aoc.part1(example5) == 11

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 19

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == 23

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc.part2(example3) == 23

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example4(example4):
    """Test part 2 on example input."""
    assert aoc.part2(example4) == 29

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example5(example5):
    """Test part 2 on example input."""
    assert aoc.part2(example5) == 26

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ""