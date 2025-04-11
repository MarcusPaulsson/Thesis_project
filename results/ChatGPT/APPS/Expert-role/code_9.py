def find_grandpas_sofa(d, n, m, sofas, counts):
    cnt_l, cnt_r, cnt_t, cnt_b = counts
    sofas_count = []

    for i in range(d):
        x1, y1, x2, y2 = sofas[i]
        left = right = top = bottom = 0
        
        # Determine the position of the current sofa
        if x1 == x2:  # Vertical sofa
            if y1 < y2:
                y1, y2 = y2, y1  # Ensure y1 < y2
            # Check for sofas to the left and right
            for j in range(d):
                if i == j:
                    continue
                x3, y3, x4, y4 = sofas[j]
                if x3 == x4:  # Vertical sofa
                    if y3 < y4:
                        y3, y4 = y4, y3  # Ensure y3 < y4
                    if x3 < x1:  # Left
                        left += 1
                    elif x3 > x1:  # Right
                        right += 1
                else:  # Horizontal sofa
                    if x3 < x1 and (y3 == y1 or y4 == y1):  # Left
                        left += 1
                    elif x3 > x1 and (y3 == y2 or y4 == y2):  # Right
                        right += 1
        else:  # Horizontal sofa
            if x1 < x2:
                x1, x2 = x2, x1  # Ensure x1 < x2
            # Check for sofas to the top and bottom
            for j in range(d):
                if i == j:
                    continue
                x3, y3, x4, y4 = sofas[j]
                if x3 == x4:  # Vertical sofa
                    if y3 < y4:
                        y3, y4 = y4, y3  # Ensure y3 < y4
                    if y3 < y1:  # Top
                        top += 1
                    elif y3 > y2:  # Bottom
                        bottom += 1
                else:  # Horizontal sofa
                    if y3 < y1 and (x3 == x1 or x4 == x1):  # Top
                        top += 1
                    elif y3 > y2 and (x3 == x2 or x4 == x2):  # Bottom
                        bottom += 1

        if left == cnt_l and right == cnt_r and top == cnt_t and bottom == cnt_b:
            sofas_count.append(i + 1)  # Store the 1-based index

    return sofas_count[0] if sofas_count else -1


# Input reading
d = int(input())
n, m = map(int, input().split())
sofas = [tuple(map(int, input().split())) for _ in range(d)]
counts = tuple(map(int, input().split()))

# Output the result
print(find_grandpas_sofa(d, n, m, sofas, counts))