d = int(input())
n, m = map(int, input().split())

sofas = []
for i in range(d):
    x1, y1, x2, y2 = map(int, input().split())
    sofas.append((x1, y1, x2, y2))

cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

def count_neighbors(sofa):
    x1, y1, x2, y2 = sofa
    left = right = top = bottom = 0
    
    for other in sofas:
        if other == sofa:
            continue
        ox1, oy1, ox2, oy2 = other
        
        if x1 == x2:  # Vertical sofa
            if oy1 < y1:  # Other sofa is above
                top += 1
            elif oy1 > y2:  # Other sofa is below
                bottom += 1
            elif ox2 < y1:  # Other sofa is to the left
                left += 1
            elif ox1 > y2:  # Other sofa is to the right
                right += 1
        else:  # Horizontal sofa
            if ox1 < x1:  # Other sofa is to the left
                left += 1
            elif ox1 > x2:  # Other sofa is to the right
                right += 1
            elif y1 == y2:  # Same row
                if ox2 < y1:  # Other sofa is above
                    top += 1
                elif oy1 > y2:  # Other sofa is below
                    bottom += 1

    return left, right, top, bottom

for i in range(d):
    left, right, top, bottom = count_neighbors(sofas[i])
    if (left == cnt_l and right == cnt_r and top == cnt_t and bottom == cnt_b):
        print(i + 1)
        break
else:
    print(-1)