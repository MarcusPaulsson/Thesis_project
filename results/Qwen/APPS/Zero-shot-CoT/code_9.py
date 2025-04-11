def find_grandpa_sofa(d, n, m, sofas, cnt_l, cnt_r, cnt_t, cnt_b):
    # Create a set to store all cells covered by sofas
    covered_cells = set()
    for i, (x1, y1, x2, y2) in enumerate(sofas):
        covered_cells.add((x1, y1))
        covered_cells.add((x2, y2))
    
    # Iterate through each sofa to check the conditions
    for i, (x1, y1, x2, y2) in enumerate(sofas):
        # Check left condition
        left_count = 0
        for j in range(1, y1):
            if (x1, j) in covered_cells or (x2, j) in covered_cells:
                left_count += 1
        
        # Check right condition
        right_count = 0
        for j in range(y1 + 1, m + 1):
            if (x1, j) in covered_cells or (x2, j) in covered_cells:
                right_count += 1
        
        # Check top condition
        top_count = 0
        for j in range(1, x1):
            if (j, y1) in covered_cells or (j, y2) in covered_cells:
                top_count += 1
        
        # Check bottom condition
        bottom_count = 0
        for j in range(x1 + 1, n + 1):
            if (j, y1) in covered_cells or (j, y2) in covered_cells:
                bottom_count += 1
        
        # If all conditions are met, return the sofa number
        if left_count == cnt_l and right_count == cnt_r and top_count == cnt_t and bottom_count == cnt_b:
            return i + 1
    
    # If no sofa meets all conditions, return -1
    return -1

# Read input
d = int(input())
n, m = map(int, input().split())
sofas = [tuple(map(int, input().split())) for _ in range(d)]
cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

# Find and print the number of Grandpa Maks's sofa
print(find_grandpa_sofa(d, n, m, sofas, cnt_l, cnt_r, cnt_t, cnt_b))