from heapq import heappop, heappush

def parse_input(file_name):
    with open(file_name, 'r') as f:
        maze = [list(line.strip()) for line in f]
    start = None
    end = None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
    return maze, start, end

def is_valid(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#'

def reindeer_maze(file_name):
    maze, start, end = parse_input(file_name)

    # Directions: (dx, dy) and direction names
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # East, South, West, North
    direction_names = ['E', 'S', 'W', 'N']

    # Priority queue for A* search
    pq = []
    heappush(pq, (0, start[0], start[1], 0))  # (cost, x, y, direction_index)

    # Visited set with state (x, y, direction_index)
    visited = set()

    while pq:
        cost, x, y, direction = heappop(pq)

        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        # If we reach the end, return the cost
        if (x, y) == end:
            return cost

        # Try moving forward
        nx, ny = x + directions[direction][0], y + directions[direction][1]
        if is_valid(maze, nx, ny):
            heappush(pq, (cost + 1, nx, ny, direction))

        # Try turning left or right
        for turn in [-1, 1]:
            new_direction = (direction + turn) % 4
            heappush(pq, (cost + 1000, x, y, new_direction))

    return -1  # Shouldn't reach here if there's a valid path

# Solve the problem
file_name = "maze.txt"
print("Lowest score:", reindeer_maze(file_name))