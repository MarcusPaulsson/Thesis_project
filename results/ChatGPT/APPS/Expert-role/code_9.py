def find_grandpa_sofa(d, n, m, sofas, cnt_l, cnt_r, cnt_t, cnt_b):
    positions = []

    # Parse the sofa positions
    for i in range(d):
        x1, y1, x2, y2 = sofas[i]
        positions.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))

    # Count sofas in each direction for each sofa
    results = []
    
    for i in range(d):
        cnt_left = cnt_right = cnt_top = cnt_bottom = 0
        for j in range(d):
            if i == j:
                continue
            x1, y1, x2, y2 = positions[i]
            a1, b1, a2, b2 = positions[j]
            if a2 < x1:  # j is to the left of i
                cnt_left += 1
            elif a1 > x2:  # j is to the right of i
                cnt_right += 1
            if b2 < y1:  # j is above i
                cnt_top += 1
            elif b1 > y2:  # j is below i
                cnt_bottom += 1
        
        # Check if the counts match the conditions
        if cnt_left == cnt_l and cnt_right == cnt_r and cnt_top == cnt_t and cnt_bottom == cnt_b:
            results.append(i + 1)  # Store 1-based index

    return results[0] if results else -1

# Input reading
d = int(input())
n, m = map(int, input().split())
sofas = [tuple(map(int, input().split())) for _ in range(d)]
cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

# Get the result
result = find_grandpa_sofa(d, n, m, sofas, cnt_l, cnt_r, cnt_t, cnt_b)
print(result)