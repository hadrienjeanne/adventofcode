# test_aoc_template.py

import pathlib
import pytest
import aoc202211 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [['Monkey 0:', '  Starting items: 79, 98', '  Operation: new = old * 19', '  Test: divisible by 23', '    If true: throw to monkey 2', '    If false: throw to monkey 3'], ['Monkey 1:', '  Starting items: 54, 65, 75, 74', '  Operation: new = old + 6', '  Test: divisible by 19', '    If true: throw to monkey 2', '    If false: throw to monkey 0'], ['Monkey 2:', '  Starting items: 79, 60, 97', '  Operation: new = old * old', '  Test: divisible by 13', '    If true: throw to monkey 1', '    If false: throw to monkey 3'], ['Monkey 3:', '  Starting items: 74', '  Operation: new = old + 3', '  Test: divisible by 17', '    If true: throw to monkey 0', '    If false: throw to monkey 1']]

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 10605

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 2713310158
