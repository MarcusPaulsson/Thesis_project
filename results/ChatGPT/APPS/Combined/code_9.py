def find_grandpa_sofa(d, n, m, sofas, conditions):
    cnt_l, cnt_r, cnt_t, cnt_b = conditions
    sofa_positions = []

    # Store the normalized positions of each sofa
    for x1, y1, x2, y2 in sofas:
        sofa_positions.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))

    # Function to count the sofas in certain directions
    def count_sofas(sofa_index):
        x1, y1, x2, y2 = sofa_positions[sofa_index]
        left_count = right_count = top_count = bottom_count = 0
        
        for j, (sx1, sy1, sx2, sy2) in enumerate(sofa_positions):
            if j == sofa_index:
                continue
            
            # Count left, right, top, and bottom
            if sx2 < x1:
                left_count += 1
            elif sx1 > x2:
                right_count += 1
            
            if sy2 < y1:
                top_count += 1
            elif sy1 > y2:
                bottom_count += 1

        return left_count, right_count, top_count, bottom_count

    # Find the sofa that matches the conditions
    for i in range(d):
        left_count, right_count, top_count, bottom_count = count_sofas(i)
        if (left_count == cnt_l and 
            right_count == cnt_r and 
            top_count == cnt_t and 
            bottom_count == cnt_b):
            return i + 1  # Return 1-based index

    return -1

# Input reading
d = int(input())
n, m = map(int, input().split())
sofas = [tuple(map(int, input().split())) for _ in range(d)]
conditions = tuple(map(int, input().split()))

# Find and print the result
result = find_grandpa_sofa(d, n, m, sofas, conditions)
print(result)