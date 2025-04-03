def find_grandpa_sofa(d, n, m, sofas, cnt_l, cnt_r, cnt_t, cnt_b):
    # To store the count of sofas in each direction with respect to each sofa
    counts = []

    for i in range(d):
        count_left = count_right = count_top = count_bottom = 0
        x1, y1, x2, y2 = sofas[i]

        # Check against all the other sofas
        for j in range(d):
            if i == j:
                continue
            x1j, y1j, x2j, y2j = sofas[j]

            # Determine the position of sofa j relative to sofa i
            if x2 < x1j:  # i is to the left of j
                count_left += 1
            elif x1 > x2j:  # i is to the right of j
                count_right += 1
            elif y2 < y1j:  # i is above j
                count_top += 1
            elif y1 > y2j:  # i is below j
                count_bottom += 1

        counts.append((count_left, count_right, count_top, count_bottom))

    # Now find the sofa that matches the required counts
    for i in range(d):
        if counts[i] == (cnt_l, cnt_r, cnt_t, cnt_b):
            return i + 1  # Return 1-based index

    return -1  # If no such sofa is found


# Read input
d = int(input())
n, m = map(int, input().split())
sofas = [tuple(map(int, input().split())) for _ in range(d)]
cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

# Call the function and print the result
result = find_grandpa_sofa(d, n, m, sofas, cnt_l, cnt_r, cnt_t, cnt_b)
print(result)