import heapq

def find_first_blocking_byte(input_file):
    # Read coordinates of falling bytes
    with open(input_file, 'r') as f:
        coordinates = [tuple(map(int, line.strip().split(','))) for line in f]

    # Define grid size and movement directions
    GRID_SIZE = 70
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Check if a path exists from start to goal
    def is_path_exists(corrupted):
        start = (0, 0)
        goal = (GRID_SIZE, GRID_SIZE)

        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            current = queue.pop(0)

            if current == goal:
                return True

            for dx, dy in DIRECTIONS:
                neighbor = (current[0] + dx, current[1] + dy)

                # Check if neighbor is valid (within grid and not corrupted)
                if (0 <= neighbor[0] <= GRID_SIZE and
                    0 <= neighbor[1] <= GRID_SIZE and
                    neighbor not in corrupted and
                    neighbor not in visited):
                    queue.append(neighbor)
                    visited.add(neighbor)

        return False

    # Track corrupted spaces and find first blocking byte
    corrupted = set()
    for i, coord in enumerate(coordinates):
        corrupted.add(coord)

        # Check if this coordinate blocks the path
        if not is_path_exists(corrupted):
            return coord

    return None  # No blocking byte found

# Read input from file and solve
result = find_first_blocking_byte('steps.txt')
print(f"First blocking byte coordinates: {result[0]},{result[1]}")
     