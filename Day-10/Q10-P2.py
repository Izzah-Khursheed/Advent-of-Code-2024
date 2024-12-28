def parse_map(file_path):
    """
    Reads the topographic map from the input file and converts it into a 2D list of integers.
    """
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def dfs_count_trails(topographic_map, r, c, visited):
    """
    Depth-first search to count distinct hiking trails that begin at (r, c) and end at 9.
    """
    rows, cols = len(topographic_map), len(topographic_map[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(r, c, [(r, c)])]  # stack holds (row, col, current_path)
    trails = set()  # To track distinct paths ending at 9

    while stack:
        cr, cc, path = stack.pop()
        current_height = topographic_map[cr][cc]

        # If we reach a height of 9, add the trail
        if current_height == 9:
            trails.add(tuple(path))
            continue

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                next_height = topographic_map[nr][nc]
                if next_height == current_height + 1 and (nr, nc) not in path:
                    stack.append((nr, nc, path + [(nr, nc)]))

    return len(trails)

def calculate_trailhead_ratings(topographic_map):
    """
    Calculates the sum of ratings for all trailheads in the topographic map.
    """
    rows, cols = len(topographic_map), len(topographic_map[0])
    total_rating = 0

    for r in range(rows):
        for c in range(cols):
            if topographic_map[r][c] == 0:  # Found a trailhead
                visited = set()
                rating = dfs_count_trails(topographic_map, r, c, visited)
                total_rating += rating

    return total_rating

def main():
    """
    Main function to load the map, compute ratings, and display the result.
    """
    file_path = "grid.txt"  # Ensure input.txt is in the same directory
    topographic_map = parse_map(file_path)
    total_rating = calculate_trailhead_ratings(topographic_map)
    print(f"Total sum of trailhead ratings: {total_rating}")

if __name__ == "__main__":
    main()