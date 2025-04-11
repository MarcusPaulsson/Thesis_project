d = int(input())
n, m = map(int, input().split())

sofas = []
for i in range(d):
    x1, y1, x2, y2 = map(int, input().split())
    sofas.append((x1, y1, x2, y2))

cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

def count_sofas(sofa, sofas):
    x1, y1, x2, y2 = sofa
    left = right = top = bottom = 0
    
    for other in sofas:
        if other == sofa:
            continue
        ox1, oy1, ox2, oy2 = other
        
        if (x1 < ox1 and x2 < ox1) or (x1 < ox2 and x2 < ox2):
            left += 1
        if (x1 > ox1 and x2 > ox1) or (x1 > ox2 and x2 > ox2):
            right += 1
        if (y1 < oy1 and y2 < oy1) or (y1 < oy2 and y2 < oy2):
            top += 1
        if (y1 > oy1 and y2 > oy1) or (y1 > oy2 and y2 > oy2):
            bottom += 1
            
    return left, right, top, bottom

for i in range(d):
    left, right, top, bottom = count_sofas(sofas[i], sofas)
    if (left == cnt_l and right == cnt_r and top == cnt_t and bottom == cnt_b):
        print(i + 1)
        break
else:
    print(-1)