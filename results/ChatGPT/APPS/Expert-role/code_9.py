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
            if ox1 == ox2:  # Other is also vertical
                if y2 < oy1:  # Other is below
                    bottom += 1
                elif oy2 < y1:  # Other is above
                    top += 1
            else:  # Other is horizontal
                if x1 < ox1:  # Other is to the right
                    right += 1
                elif ox1 < x1:  # Other is to the left
                    left += 1
        else:  # Horizontal sofa
            if ox1 == ox2:  # Other is vertical
                if y1 < oy1:  # Other is below
                    bottom += 1
                elif oy2 < y1:  # Other is above
                    top += 1
            else:  # Other is also horizontal
                if y1 < oy1:  # Other is below
                    bottom += 1
                elif oy1 < y1:  # Other is above
                    top += 1

    return left, right, top, bottom

for i in range(d):
    left, right, top, bottom = count_neighbors(sofas[i])
    if left == cnt_l and right == cnt_r and top == cnt_t and bottom == cnt_b:
        print(i + 1)
        break
else:
    print(-1)