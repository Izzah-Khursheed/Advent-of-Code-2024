def check_diagonal(grid, r, c, dr, dc, pattern):
    """Check if a diagonal contains the given pattern (MAS or SAM)"""
    try:
        return (grid[r][c] == pattern[0] and
                grid[r + dr][c + dc] == pattern[1] and
                grid[r + 2*dr][c + 2*dc] == pattern[2])
    except IndexError:
        return False

def check_x_mas_at_position(grid, r, c):
    """Check if there's an X-MAS pattern centered at position (r,c)"""
    if grid[r][c] != 'A':  # Center must be 'A'
        return False
        
    patterns = ['MAS', 'SAM']  # Both forward and backward patterns
    
    # Check all possible combinations of patterns for both diagonals
    for p1 in patterns:
        for p2 in patterns:
            # Check top-left to bottom-right diagonal with p1
            diagonal1 = check_diagonal(grid, r-1, c-1, 1, 1, p1)
            # Check top-right to bottom-left diagonal with p2
            diagonal2 = check_diagonal(grid, r-1, c+1, 1, -1, p2)
            
            if diagonal1 and diagonal2:
                return True
                
    return False

def count_x_mas(grid):
    """Count total number of X-MAS patterns in the grid"""
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    
    # Print input grid for debugging
    print("Input Grid:")
    for row in grid:
        print(row)
    print()
    
    # Need at least 3x3 grid for an X pattern
    if rows < 3 or cols < 3:
        return 0
        
    # Check each possible center position
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if check_x_mas_at_position(grid, r, c):
                print(f"Found X-MAS pattern at center ({r},{c})")
                count += 1
                
    return count

def main():
    try:
        # Read the puzzle input
        with open("word_search.txt") as f:
            grid = [line.strip() for line in f]
            
        # Count the number of X-MAS patterns
        result = count_x_mas(grid)
        print(f"\nTotal X-MAS patterns found: {result}")
        
    except FileNotFoundError:
        print("Error: Could not open input file")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()