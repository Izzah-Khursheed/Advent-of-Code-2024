def find_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    regions = []

    def dfs(r, c, plant_type):
        if (r, c) in visited or r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != plant_type:
            return set()

        cells = {(r, c)}
        visited.add((r, c))

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            cells.update(dfs(r + dr, c + dc, plant_type))

        return cells

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                region = dfs(r, c, grid[r][c])
                if region:
                    regions.append(region)

    return regions

def count_sides(region, grid):
    rows, cols = len(grid), len(grid[0])
    sides = 0
    visited_edges = set()

    def trace_line(r, c, dr, dc):
        nr, nc = r + dr, c + dc
        return (nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) not in region)

    # Count horizontal lines
    for r, c in region:
        # Check up
        if (r, c, 'u') not in visited_edges and trace_line(r, c, -1, 0):
            start_c = c
            while (r, start_c-1) in region and trace_line(r, start_c-1, -1, 0):
                start_c -= 1
            end_c = c
            while (r, end_c+1) in region and trace_line(r, end_c+1, -1, 0):
                end_c += 1
            sides += 1
            for i in range(start_c, end_c+1):
                visited_edges.add((r, i, 'u'))

        # Check down
        if (r, c, 'd') not in visited_edges and trace_line(r, c, 1, 0):
            start_c = c
            while (r, start_c-1) in region and trace_line(r, start_c-1, 1, 0):
                start_c -= 1
            end_c = c
            while (r, end_c+1) in region and trace_line(r, end_c+1, 1, 0):
                end_c += 1
            sides += 1
            for i in range(start_c, end_c+1):
                visited_edges.add((r, i, 'd'))

    # Count vertical lines
    for r, c in region:
        # Check left
        if (r, c, 'l') not in visited_edges and trace_line(r, c, 0, -1):
            start_r = r
            while (start_r-1, c) in region and trace_line(start_r-1, c, 0, -1):
                start_r -= 1
            end_r = r
            while (end_r+1, c) in region and trace_line(end_r+1, c, 0, -1):
                end_r += 1
            sides += 1
            for i in range(start_r, end_r+1):
                visited_edges.add((i, c, 'l'))

        # Check right
        if (r, c, 'r') not in visited_edges and trace_line(r, c, 0, 1):
            start_r = r
            while (start_r-1, c) in region and trace_line(start_r-1, c, 0, 1):
                start_r -= 1
            end_r = r
            while (end_r+1, c) in region and trace_line(end_r+1, c, 0, 1):
                end_r += 1
            sides += 1
            for i in range(start_r, end_r+1):
                visited_edges.add((i, c, 'r'))

    return sides

def solve_part2(input_text):
    grid = [list(line.strip()) for line in input_text.strip().split('\n')]
    regions = find_regions(grid)

    total_price = 0
    for region in regions:
        area = len(region)
        num_sides = count_sides(region, grid)
        price = area * num_sides
        total_price += price

    return total_price

with open('map.txt', 'r') as f:
    input_text = f.read()

result = solve_part2(input_text)
print(result)