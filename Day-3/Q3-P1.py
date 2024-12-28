import re

# Define the file path
file_path = "memory.txt"  # Replace with the actual file path

# Function to process the corrupted memory and calculate the sum of valid multiplications
def calculate_multiplications(file_path):
    # Read the file
    with open(file_path, "r") as file:
        data = file.read()
    
    # Define the regex pattern for valid mul instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all matches
    matches = re.findall(pattern, data)
    
    # Calculate the sum of all valid multiplications
    total = 0
    for x, y in matches:
        total += int(x) * int(y)
    
    return total

# Calculate and print the result
result = calculate_multiplications(file_path)
print("Sum of all valid multiplications:", result)
