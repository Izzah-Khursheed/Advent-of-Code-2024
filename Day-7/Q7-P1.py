
from itertools import product

def parse_input(file_path):
    """
    Parse the input file into target values and numbers for each equation.
    """
    equations = []
    with open(file_path, 'r') as f:
        for line in f:
            target, nums = line.strip().split(':')
            target = int(target)
            numbers = list(map(int, nums.split()))
            equations.append((target, numbers))
    return equations


def evaluate_expression(numbers, operators):
    """
    Evaluate the expression given the numbers and operators, following left-to-right evaluation.
    """
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result


def find_valid_equations(equations):
    """
    Find all valid equations and calculate their total calibration result.
    """
    total_calibration = 0

    for target, numbers in equations:
        # Generate all possible operator combinations
        num_operators = len(numbers) - 1
        operator_combinations = product(['+', '*'], repeat=num_operators)

        # Check each operator combination
        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == target:
                total_calibration += target
                break  # No need to check further combinations for this equation

    return total_calibration


def solve(file_path):
    """
    Main function to solve the problem.
    """
    equations = parse_input(file_path)
    result = find_valid_equations(equations)
    return result


# File path to the input file
input_file = 'equations.txt'

# Solve the problem
result = solve(input_file)
print(f"Total calibration result: {result}")
