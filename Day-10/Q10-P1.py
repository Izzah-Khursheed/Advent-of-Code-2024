from typing import List, Tuple, Set

def read_input(filename: str) -> List[List[int]]:
    """Read the input file and convert it to a 2D list of integers."""
    with open(filename, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def find_trail_to_nine(grid: List[List[int]], start: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Find all 9-height positions reachable from a trailhead via a valid hiking trail.
    """
    rows, cols = len(grid), len(grid[0])
    nine_positions = []

    def dfs(x: int, y: int, current_height: int, path: Set[Tuple[int, int]]) -> None:
        # If we've reached height 9, this is a valid trail
        if grid[x][y] == 9:
            nine_positions.append((x, y))
            return

        # Possible moves: up, down, left, right
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy

            # Check if new cell is within grid and a valid next step
            if (0 <= nx < rows and 0 <= ny < cols and
                (nx, ny) not in path and
                grid[nx][ny] == current_height + 1):
                # Create a new path including this step
                new_path = path.copy()
                new_path.add((nx, ny))
                # Continue the trail
                dfs(nx, ny, grid[nx][ny], new_path)

    # Start the search from the trailhead
    dfs(start[0], start[1], grid[start[0]][start[1]], {start})

    return nine_positions

def solve_trailheads(grid: List[List[int]]) -> int:
    """
    Find all trailheads and calculate their scores.
    """
    rows, cols = len(grid), len(grid[0])
    trailhead_scores = []

    # Find all trailheads (positions with height 0)
    trailheads = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

    # Calculate score for each trailhead
    for trailhead in trailheads:
        # Find unique 9-height positions reachable from this trailhead
        reachable_nines = set(find_trail_to_nine(grid, trailhead))
        trailhead_scores.append(len(reachable_nines))

    # Verbose output for debugging
    print("Trailhead Scores:", trailhead_scores)

    return sum(trailhead_scores)

def main():
    # Read input from file
    grid = read_input('grid.txt')

    # Solve and print the total trailhead score
    total_score = solve_trailheads(grid)
    print(f"Sum of trailhead scores: {total_score}")

if __name__ == "__main__":
    main()