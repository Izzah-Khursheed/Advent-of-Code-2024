def find_solution(a1, a2, b1, b2, target_x, target_y):
    # Calculate determinant
    det = a1 * b2 - a2 * b1

    if det == 0:
        return None

    # Using Cramer's rule
    n = (target_x * b2 - target_y * b1) / det
    m = (a1 * target_y - a2 * target_x) / det

    # Check if solution is integer and non-negative
    if n != int(n) or m != int(m) or n < 0 or m < 0:
        return None

    n = int(n)
    m = int(m)

    # Verify solution
    if (a1 * n + b1 * m == target_x) and (a2 * n + b2 * m == target_y):
        return (n, m)

    return None

def solve_claw_machines_part2(input_data):
    total_tokens = 0
    possible_prizes = 0
    OFFSET = 10000000000000

    lines = input_data.strip().split('\n')

    for i in range(0, len(lines), 4):
        if i + 2 >= len(lines):
            break

        # Parse input
        a_line = lines[i].strip()
        ax = int(a_line[a_line.find('X+')+2:a_line.find(',')])
        ay = int(a_line[a_line.find('Y+')+2:])

        b_line = lines[i+1].strip()
        bx = int(b_line[b_line.find('X+')+2:b_line.find(',')])
        by = int(b_line[b_line.find('Y+')+2:])

        p_line = lines[i+2].strip()
        px = int(p_line[p_line.find('X=')+2:p_line.find(',')]) + OFFSET
        py = int(p_line[p_line.find('Y=')+2:]) + OFFSET

        # Find solution
        solution = find_solution(ax, ay, bx, by, px, py)

        if solution:
            n, m = solution
            tokens = 3 * n + m
            total_tokens += tokens
            possible_prizes += 1

    return total_tokens, possible_prizes

# Read input from file
with open('token.txt', 'r') as file:
    input_data = file.read()

total_tokens, possible_prizes = solve_claw_machines_part2(input_data)
print(f"Total possible prizes: {possible_prizes}")
print(f"Total tokens needed (this is the answer): {total_tokens}")