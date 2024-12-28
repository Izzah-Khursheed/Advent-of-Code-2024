def parse_schematic(lines):
    # Get the width of the schematic
    width = len(lines[0])
    heights = []

    # For each column
    for col in range(width):
        # Find height by counting from appropriate direction
        height = 0
        # For locks (filled from top), count empty spaces from top
        if lines[0][col] == '#':
            for row in range(len(lines)):
                if lines[row][col] == '#':
                    height += 1
            heights.append(height)
        # For keys (filled from bottom), count filled spaces from bottom
        else:
            for row in range(len(lines)-1, -1, -1):
                if lines[row][col] == '#':
                    height += 1
            heights.append(height)
    return heights

def can_fit(lock_heights, key_heights):
    # Check if any column overlaps
    # Available space is len(schematic) - 1
    max_height = 7  # Based on input format
    for lock_h, key_h in zip(lock_heights, key_heights):
        if lock_h + key_h > max_height:
            return False
    return True

def solve_lock_key_pairs(input_text):
    # Split input into blocks separated by empty lines
    blocks = input_text.strip().split('\n\n')

    locks = []
    keys = []

    # Parse each block
    for block in blocks:
        lines = block.strip().split('\n')
        # If top row is filled, it's a lock
        if lines[0].count('#') > 0:
            locks.append(parse_schematic(lines))
        # If bottom row is filled, it's a key
        elif lines[-1].count('#') > 0:
            keys.append(parse_schematic(lines))

    # Count fitting pairs
    fitting_pairs = 0
    for lock in locks:
        for key in keys:
            if can_fit(lock, key):
                fitting_pairs += 1

    return fitting_pairs

# Read input from file
with open('final.txt', 'r') as file:
    input_text = file.read()

result = solve_lock_key_pairs(input_text)
print(f"Number of unique lock/key pairs that fit: {result}")