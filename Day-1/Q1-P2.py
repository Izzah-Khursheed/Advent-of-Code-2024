from collections import Counter


def calculate_similarity_score(file_name):
    with open(file_name, 'r') as f:
        # Read the file content and clean up the extra spaces
        content = f.read().strip().splitlines()

        # Separate the left and right lists
        left_list = []
        right_list = []

        # Reading numbers from the file into two lists
        for line in content:
            num1, num2 = map(int, line.split())
            left_list.append(num1)
            right_list.append(num2)

    # Count the occurrences of each number in the right list
    right_count = Counter(right_list)

    # Calculate the similarity score
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_count.get(number, 0)

    return similarity_score


# Input file name
file_name = "input.txt"

# Calculate and print the similarity score
score = calculate_similarity_score(file_name)
print("Similarity Score:", score)





# Define the file path
# file_path = "input.txt"  # Replace with your file's actual path

# # Read the file
# with open(file_path, "r") as file:
#     lines = file.readlines()

# # Split the input into two lists
# left_list = []
# right_list = []

# for line in lines:
#     left, right = map(int, line.split())
#     left_list.append(left)
#     right_list.append(right)

# # Count the occurrences of each number in the right list
# from collections import Counter
# right_counter = Counter(right_list)

# # Calculate the similarity score
# similarity_score = 0

# for number in left_list:
#     similarity_score += number * right_counter[number]

# print("Similarity Score:", similarity_score)
