import math

def parse_input(file_path):
    with open(file_path, "r") as file:
        data = file.read().strip().split("\n\n")

    machines = []
    for block in data:
        lines = block.split("\n")
        button_a = tuple(map(int, lines[0].split("X+")[1].split(", Y+")))
        button_b = tuple(map(int, lines[1].split("X+")[1].split(", Y+")))
        prize = tuple(map(int, lines[2].split("X=")[1].split(", Y=")))
        machines.append((button_a, button_b, prize))

    return machines

def solve_claw_machine(button_a, button_b, prize):
    a, c = button_a
    b, d = button_b
    X, Y = prize

    min_cost = float('inf')
    best_na, best_nb = None, None

    # Iterate over possible n_A values
    for n_A in range(101):
        rem_x = X - n_A * a
        rem_y = Y - n_A * c

        if rem_x % b == 0 and rem_y % d == 0:
            n_B_x = rem_x // b
            n_B_y = rem_y // d

            if n_B_x == n_B_y and n_B_x >= 0:
                cost = 3 * n_A + n_B_x
                if cost < min_cost:
                    min_cost = cost
                    best_na, best_nb = n_A, n_B_x

    return min_cost if best_na is not None else None

def main(file_path):
    machines = parse_input(file_path)
    total_cost = 0
    prizes_won = 0

    for button_a, button_b, prize in machines:
        result = solve_claw_machine(button_a, button_b, prize)
        if result is not None:
            total_cost += result
            prizes_won += 1

    print(f"Prizes Won: {prizes_won}")
    print(f"Minimum Tokens Spent: {total_cost}")

# Example usage
main("token.txt")
