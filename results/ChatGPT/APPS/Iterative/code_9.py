d = int(input())
n, m = map(int, input().split())

sofas = []
for _ in range(d):
    x1, y1, x2, y2 = map(int, input().split())
    sofas.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))

cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

def count_situation(sofa):
    x1, y1, x2, y2 = sofa
    left = right = top = bottom = 0
    
    for other in sofas:
        if other == sofa:
            continue
        ox1, oy1, ox2, oy2 = other
        
        if x2 < ox1:  # Sofa is to the left
            left += 1
        if x1 > ox2:  # Sofa is to the right
            right += 1
        if y2 < oy1:  # Sofa is on top
            top += 1
        if y1 > oy2:  # Sofa is below
            bottom += 1
    
    return left, right, top, bottom

for i in range(d):
    left, right, top, bottom = count_situation(sofas[i])
    if (left == cnt_l) and (right == cnt_r) and (top == cnt_t) and (bottom == cnt_b):
        print(i + 1)
        break
else:
    print(-1)