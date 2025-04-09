def find_grandpa_sofa(d, n, m, sofas, counts):
    cnt_l, cnt_r, cnt_t, cnt_b = counts
    for i in range(d):
        count_left = count_right = count_top = count_bottom = 0
        
        x1, y1, x2, y2 = sofas[i]
        
        # Check for counts to the left
        for j in range(d):
            if j != i:
                x1_j, y1_j, x2_j, y2_j = sofas[j]
                if x1_j == x2_j:  # Same column
                    if y2_j < y1:  # Sofa j is to the left of sofa i
                        count_left += 1
                elif y1_j == y2_j:  # Same row
                    if x2_j < x1:  # Sofa j is above sofa i
                        count_top += 1
                elif x1_j == x2_j:  # Same column
                    if y1 < y1_j:  # Sofa j is to the right of sofa i
                        count_right += 1
                elif y1_j == y2_j:  # Same row
                    if x1 < x2_j:  # Sofa j is below sofa i
                        count_bottom += 1
        
        if (count_left == cnt_l and
            count_right == cnt_r and
            count_top == cnt_t and
            count_bottom == cnt_b):
            return i + 1  # Return 1-based index

    return -1  # If no such sofa is found

# Input reading
d = int(input())
n, m = map(int, input().split())
sofas = [tuple(map(int, input().split())) for _ in range(d)]
counts = tuple(map(int, input().split()))

# Output the result
result = find_grandpa_sofa(d, n, m, sofas, counts)
print(result)