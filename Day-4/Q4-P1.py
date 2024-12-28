def count_xmas_occurrences(file_path):
    # Read the grid from the file
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    
    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"
    word_len = len(target)
    count = 0

    # Define all 8 possible directions (row_change, col_change)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
        (-1, -1)  # Diagonal up-left
    ]

    # Helper function to check if a word exists in a given direction
    def check_word(row, col, direction):
        for i in range(word_len):
            r, c = row + i * direction[0], col + i * direction[1]
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != target[i]:
                return False
        return True

    # Iterate through each cell of the grid
    for row in range(rows):
        for col in range(cols):
            # Check for the word in all directions
            for direction in directions:
                if check_word(row, col, direction):
                    count += 1

    return count

# Example usage
file_path = "word_search.txt"  # Replace with the actual file path
result = count_xmas_occurrences(file_path)
print("Total occurrences of XMAS:", result)
