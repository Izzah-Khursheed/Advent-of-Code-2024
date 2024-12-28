from collections import deque

def read_input(file_path):
    with open(file_path, "r") as file:
        return [tuple(map(int, line.strip().split(','))) for line in file]

def simulate_corruption(grid, corrupted_positions):
    for x, y in corrupted_positions:
        grid[y][x] = "#"

def bfs_shortest_path(grid, start, goal):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
    visited = set()
    visited.add(start)

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == goal:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 71 and 0 <= ny < 71 and (nx, ny) not in visited and grid[ny][nx] == ".":
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    return -1  # If no path exists

def main():
    # Initialize the grid
    grid_size = 71
    grid = [["."] * grid_size for _ in range(grid_size)]

    # Read input and simulate falling bytes
    corrupted_positions = read_input("steps.txt")[:1024]
    simulate_corruption(grid, corrupted_positions)

    # Find shortest path
    start = (0, 0)
    goal = (70, 70)
    result = bfs_shortest_path(grid, start, goal)

    print("Minimum number of steps:", result)

if __name__ == "__main__":
    main()
