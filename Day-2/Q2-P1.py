# Define the file path
file_path = "report.txt"  # Replace with the actual file path

# Function to check if a report is safe
def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    # Check if the differences are either all positive (increasing) or all negative (decreasing)
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)
    
    # Check if all differences are within the range [1, 3]
    are_differences_valid = all(1 <= abs(diff) <= 3 for diff in differences)
    
    # Return True if both conditions are satisfied
    return (is_increasing or is_decreasing) and are_differences_valid

# Read the file and process the reports
with open(file_path, "r") as file:
    reports = file.readlines()

# Count the number of safe reports
safe_count = 0

for line in reports:
    levels = list(map(int, line.split()))  # Convert the line into a list of integers
    if is_safe(levels):
        safe_count += 1

print("Number of Safe Reports:", safe_count)
