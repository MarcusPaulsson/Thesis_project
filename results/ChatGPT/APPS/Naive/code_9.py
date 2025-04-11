def find_grandpa_sofa(d, n, m, sofas, counts):
    cnt_l, cnt_r, cnt_t, cnt_b = counts
    sofas_count = []

    for i in range(d):
        x1, y1, x2, y2 = sofas[i]
        left_count = right_count = top_count = bottom_count = 0
        
        for j in range(d):
            if i == j:
                continue
            x1_j, y1_j, x2_j, y2_j = sofas[j]
            if x1 < x1_j:  # Sofa A is to the left of Sofa B
                left_count += 1
            if x1_j < x1:  # Sofa B is to the left of Sofa A
                right_count += 1
            if y1 < y1_j:  # Sofa A is above Sofa B
                top_count += 1
            if y1_j < y1:  # Sofa B is above Sofa A
                bottom_count += 1
        
        if (left_count == cnt_l and right_count == cnt_r and
                top_count == cnt_t and bottom_count == cnt_b):
            return i + 1  # Return 1-based index

    return -1

# Input reading
d = int(input())
n, m = map(int, input().split())
sofas = [tuple(map(int, input().split())) for _ in range(d)]
counts = tuple(map(int, input().split()))

# Output the result
print(find_grandpa_sofa(d, n, m, sofas, counts))