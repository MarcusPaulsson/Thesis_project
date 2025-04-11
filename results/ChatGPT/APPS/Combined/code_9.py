def find_grandpas_sofa(d, n, m, sofas, counts):
    cnt_l, cnt_r, cnt_t, cnt_b = counts

    for i in range(d):
        x1, y1, x2, y2 = sofas[i]
        
        left_count = sum(1 for j in range(d) if j != i and (sofas[j][0] < x1 and sofas[j][1] == y1 or sofas[j][0] < x2 and sofas[j][1] == y2))
        right_count = sum(1 for j in range(d) if j != i and (sofas[j][0] > x1 and sofas[j][1] == y1 or sofas[j][0] > x2 and sofas[j][1] == y2))
        top_count = sum(1 for j in range(d) if j != i and (sofas[j][0] == x1 and sofas[j][1] < y1 or sofas[j][0] == x2 and sofas[j][1] < y2))
        bottom_count = sum(1 for j in range(d) if j != i and (sofas[j][0] == x1 and sofas[j][1] > y1 or sofas[j][0] == x2 and sofas[j][1] > y2))

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
print(find_grandpas_sofa(d, n, m, sofas, counts))