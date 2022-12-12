# aoc_template.py

from copy import deepcopy
from dataclasses import dataclass
import math
import pathlib
import sys
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=11)

@dataclass
class Monkey:
    items: list[int]
    operation: str
    test_divisible: int
    target: tuple[int, int]

def parse(puzzle_input):
    """Parse input."""
    print([i.split('\n') for i in puzzle_input.split('\n\n')])
    return [i.split('\n') for i in puzzle_input.split('\n\n')]

def part1(data):
    """Solve part 1."""
    # monkeys = {}
    # # first loop through data to create monkeys
    # for monkey in data:
    #     name = int(monkey[0].split(' ')[1].strip(':'))
    #     monkeys[name] = [[], 0]
    #     items = monkey[1].split(' ')
    #     for item in items[4:]:            
    #         monkeys[name][0].append(int(item.strip(',')))

    # for round in range(20):
    #     for monkey in data:    
    #         name = int(monkey[0].split(' ')[1].strip(':'))
    #         operation = monkey[2].split(' ')[5:]
            
    #         test_divisible = int(monkey[3].split(' ')[5])
    #         monkey_if_true = int(monkey[4].split(' ')[9])
    #         monkey_if_false = int(monkey[5].split(' ')[9])
        
    #         for item in monkeys[name][0]:                
    #             monkeys[name][1] += 1
    #             # monkey inspects item, calculation of worry level
    #             # print(f"Monkey {name} inspects an item with a worry level of {item}.")                
    #             nb_old = operation.count('old')
    #             if operation[1] == '*':
    #                 if nb_old == 2:
    #                     worry_level = item * item
    #                 else:
    #                     worry_level = item * int(operation[2])
    #                 # print(f"Worry level is multiplied by {operation[2]} to {worry_level}.")
    #             elif operation[1] == '+':
    #                 if nb_old == 2:
    #                     worry_level = item + item
    #                 else:
    #                     worry_level = item + int(operation[2])
    #                 # print(f"Worry level increases by {operation[2]} to {worry_level}.")
    #             else:
    #                 raise ValueError(f"operator is unknown: {operation[1]}")
                
    #             # monkey gets bored, division by three of the worry level
    #             worry_level = worry_level // 3
    #             # print(f"Monkey gets bored with item. Worry level is divided by 3 to {worry_level}.")

    #             # test 
    #             if worry_level % test_divisible == 0:
    #                 # print(f"Current worry level is divisible by {test_divisible}.")
    #                 monkeys[monkey_if_true][0].append(worry_level)
    #                 # print(f"Item with worry level {worry_level} is thrown to monkey {monkey_if_true}.")
    #             else:
    #                 # print(f"Current worry level is not divisible by {test_divisible}.")
    #                 monkeys[monkey_if_false][0].append(worry_level)
    #                 # print(f"Item with worry level {worry_level} is thrown to monkey {monkey_if_false}.")
    #         monkeys[name][0].clear()

    # return math.prod(monkeys[x][1] for x in sorted(monkeys, key=lambda x:monkeys[x][1], reverse=True)[:2])
    monkeys = []
    counters = []
    # first loop through data to create monkeys
    for monkey in data:
        name = int(monkey[0].split(' ')[1].strip(':'))
        # monkeys.append([])
        
        items_split = monkey[1].split(' ')
        items = []
        for item in items_split[4:]:            
            items.append(int(item.strip(',')))

        name = int(monkey[0].split(' ')[1].strip(':'))
        operation = monkey[2].split('=')[-1].strip()
        
        test_divisible = int(monkey[3].split(' ')[5])
        monkey_if_true = int(monkey[4].split(' ')[9])
        monkey_if_false = int(monkey[5].split(' ')[9])

        monkeys.append(Monkey(items, operation, test_divisible, (monkey_if_true, monkey_if_false)))
        counters.append(0)

    monkeys = deepcopy(monkeys)

    for round in range(20):
        for i, monkey in enumerate(monkeys):
            while monkey.items:
                counters[i] += 1
                old = monkey.items.pop(0)
                worry_level = eval(monkey.operation)

                print(f"Monkey {i} inspects an item with a worry level of {old}.")
                print(f"Worry level operation: {monkey.operation} -> {worry_level}")
                worry_level = worry_level // 3
                print(f"Monkey gets bored with item. Worry level is divided by 3 to {worry_level}.")

                if worry_level % monkey.test_divisible == 0:
                    print(f"Current worry level is divisible by {test_divisible}.")
                    monkeys[monkey.target[0]].items.append(worry_level)
                    print(f"Item with worry level {worry_level} is thrown to monkey {monkey_if_true}.")
                else:
                    print(f"Current worry level is not divisible by {test_divisible}.")
                    monkeys[monkey.target[1]].items.append(worry_level)
                    print(f"Item with worry level {worry_level} is thrown to monkey {monkey_if_false}.")

    return math.prod(sorted(counters, reverse=True)[:2])    

                

def part2(data):
    """Solve part 2."""
    monkeys = []
    counters = []
    # first loop through data to create monkeys
    for monkey in data:
        name = int(monkey[0].split(' ')[1].strip(':'))
        # monkeys.append([])
        
        items_split = monkey[1].split(' ')
        items = []
        for item in items_split[4:]:            
            items.append(int(item.strip(',')))

        name = int(monkey[0].split(' ')[1].strip(':'))
        operation = monkey[2].split('=')[-1].strip()
        
        test_divisible = int(monkey[3].split(' ')[5])
        monkey_if_true = int(monkey[4].split(' ')[9])
        monkey_if_false = int(monkey[5].split(' ')[9])

        monkeys.append(Monkey(items, operation, test_divisible, (monkey_if_true, monkey_if_false)))
        counters.append(0)

    monkeys = deepcopy(monkeys)

    divisor = 1
    for m in monkeys:
        divisor *= m.test_divisible

    for round in range(10000):
        for i, monkey in enumerate(monkeys):
            while monkey.items:
                counters[i] += 1
                old = monkey.items.pop(0)
                worry_level = eval(monkey.operation)
                worry_level %= divisor

                if worry_level % monkey.test_divisible == 0:
                    # print(f"Current worry level is divisible by {test_divisible}.")
                    monkeys[monkey.target[0]].items.append(worry_level)
                    # print(f"Item with worry level {worry_level} is thrown to monkey {monkey_if_true}.")
                else:
                    # print(f"Current worry level is not divisible by {test_divisible}.")
                    monkeys[monkey.target[1]].items.append(worry_level)
                    # print(f"Item with worry level {worry_level} is thrown to monkey {monkey_if_false}.")
        if round % 1000 == 0 or round == 1 or round == 20:
            for k, value in enumerate(counters):
                print(f"Monkey {k} inspected items {value} times.")
    print(counters)
    return math.prod(sorted(counters, reverse=True)[:2])    


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
    