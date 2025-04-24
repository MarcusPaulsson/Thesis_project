def find_grandpa_sofa(d, n, m, sofas, counts):
    cnt_l, cnt_r, cnt_t, cnt_b = counts

    for i in range(d):
        left_count = right_count = top_count = bottom_count = 0
        x1_i, y1_i, x2_i, y2_i = sofas[i]

        for j in range(d):
            if i == j:
                continue
            x1_j, y1_j, x2_j, y2_j = sofas[j]

            if x2_i < x1_j:  # Sofa i is to the left of sofa j
                left_count += 1
            elif x1_i > x2_j:  # Sofa j is to the left of sofa i
                right_count += 1
            if y2_i < y1_j:  # Sofa i is above sofa j
                top_count += 1
            elif y1_i > y2_j:  # Sofa j is above sofa i
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