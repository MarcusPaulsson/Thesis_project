def find_grandpa_sofa(d, n, m, sofas, cnt_l, cnt_r, cnt_t, cnt_b):
    # Function to count sofas based on the position relative to the given sofa
    def count_sofas(pos, sofas):
        left, right, top, bottom = 0, 0, 0, 0
        for i, (x1, y1, x2, y2) in enumerate(sofas):
            if pos == (x1, y1) or pos == (x2, y2):
                continue
            if x1 == x2:  # Same row
                if y1 < y2:  # Sofa is to the right
                    if pos[1] < y1:  # Count left
                        left += 1
                    elif pos[1] > y2:  # Count right
                        right += 1
                else:  # Sofa is to the left
                    if pos[1] < y2:  # Count left
                        left += 1
                    elif pos[1] > y1:  # Count right
                        right += 1
            else:  # Different rows
                if y1 == y2:  # Same column
                    if x1 < x2:  # Sofa is below
                        if pos[0] < x1:  # Count top
                            top += 1
                        elif pos[0] > x2:  # Count bottom
                            bottom += 1
                    else:  # Sofa is above
                        if pos[0] < x2:  # Count top
                            top += 1
                        elif pos[0] > x1:  # Count bottom
                            bottom += 1
        return left, right, top, bottom

    for i in range(d):
        pos1 = (sofas[i][0], sofas[i][1])
        pos2 = (sofas[i][2], sofas[i][3])
        count1 = count_sofas(pos1, sofas)
        count2 = count_sofas(pos2, sofas)
        
        if count1 == (cnt_l, cnt_r, cnt_t, cnt_b) or count2 == (cnt_l, cnt_r, cnt_t, cnt_b):
            return i + 1  # Return the 1-based index
    
    return -1  # No matching sofa found

# Input reading
d = int(input())
n, m = map(int, input().split())
sofas = [tuple(map(int, input().split())) for _ in range(d)]
cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

# Function call and output the result
result = find_grandpa_sofa(d, n, m, sofas, cnt_l, cnt_r, cnt_t, cnt_b)
print(result)