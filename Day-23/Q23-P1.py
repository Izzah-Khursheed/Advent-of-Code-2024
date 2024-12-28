# Read the input from the file
with open("name.txt", "r") as file:
    connections = [line.strip() for line in file.readlines()]

# Parse connections into a graph representation
from collections import defaultdict

graph = defaultdict(set)
for connection in connections:
    a, b = connection.split('-')
    graph[a].add(b)
    graph[b].add(a)

# Find all sets of three inter-connected computers
triangles = set()
for node in graph:
    for neighbor1 in graph[node]:
        for neighbor2 in graph[node]:
            if neighbor1 != neighbor2 and neighbor2 in graph[neighbor1]:
                triangle = tuple(sorted([node, neighbor1, neighbor2]))
                triangles.add(triangle)

# Filter triangles where at least one name starts with "t"
filtered_triangles = [t for t in triangles if any(name.startswith('t') for name in t)]

# Output the result
print(f"Total triangles with at least one computer starting with 't': {len(filtered_triangles)}")