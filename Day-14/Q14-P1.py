def parse_input(filename):
    """Parse the input file to extract robot positions and velocities."""
    robots = []
    with open(filename, "r") as file:
        for line in file:
            if line.strip():
                p_part, v_part = line.split("v=")
                px, py = map(int, p_part.strip()[2:].split(","))
                vx, vy = map(int, v_part.strip().split(","))
                robots.append(((px, py), (vx, vy)))
    return robots

def simulate_robots(robots, width, height, time):
    """Simulate the positions of robots after a given time."""
    final_positions = []
    for (px, py), (vx, vy) in robots:
        x = (px + time * vx) % width
        y = (py + time * vy) % height
        final_positions.append((x, y))
    return final_positions

def count_quadrants(positions, width, height):
    """Count the number of robots in each quadrant."""
    q1, q2, q3, q4 = 0, 0, 0, 0
    mid_x, mid_y = width // 2, height // 2

    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue  # Skip robots on the middle lines
        if x < mid_x and y < mid_y:
            q1 += 1
        elif x >= mid_x and y < mid_y:
            q2 += 1
        elif x < mid_x and y >= mid_y:
            q3 += 1
        elif x >= mid_x and y >= mid_y:
            q4 += 1

    return q1, q2, q3, q4

def calculate_safety_factor(robots, width, height, time):
    """Calculate the safety factor after the given time."""
    final_positions = simulate_robots(robots, width, height, time)
    q1, q2, q3, q4 = count_quadrants(final_positions, width, height)
    return q1 * q2 * q3 * q4

def main():
    filename = "factor.txt"
    width, height = 101, 103
    time = 100

    robots = parse_input(filename)
    safety_factor = calculate_safety_factor(robots, width, height, time)
    print(f"Safety Factor: {safety_factor}")

if __name__ == "__main__":
    main()