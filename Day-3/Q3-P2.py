import re

# Define the file path
file_path = "memory.txt"  # Replace with the actual file path

# Function to process the corrupted memory and calculate the sum of enabled multiplications
def calculate_conditional_multiplications(file_path):
    # Read the file
    with open(file_path, "r") as file:
        data = file.read()
    
    # Define the regex patterns
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"  # Combined pattern for all relevant instructions
    
    # Find all matches sequentially
    matches = re.finditer(pattern, data)
    
    # Process the instructions
    mul_enabled = True  # By default, mul instructions are enabled
    total = 0

    for match in matches:
        if match.group(1) and match.group(2):  # If it's a mul(X, Y) instruction
            if mul_enabled:
                x, y = int(match.group(1)), int(match.group(2))
                total += x * y
        elif match.group(0) == "do()":  # If it's a do() instruction
            mul_enabled = True
        elif match.group(0) == "don't()":  # If it's a don't() instruction
            mul_enabled = False

    return total

# Calculate and print the result
result = calculate_conditional_multiplications(file_path)
print("Sum of all enabled multiplications:", result)
