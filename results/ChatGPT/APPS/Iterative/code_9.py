d = int(input())
n, m = map(int, input().split())
sofas = []

for _ in range(d):
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
        if x2 < ox1:  # sofa is to the left
            left += 1
        elif x1 > ox2:  # sofa is to the right
            right += 1
        elif y2 < oy1:  # sofa is above
            top += 1
        elif y1 > oy2:  # sofa is below
            bottom += 1
            
    return left, right, top, bottom

for i in range(d):
    left, right, top, bottom = count_sofas(sofas[i], sofas)
    if (left, right, top, bottom) == (cnt_l, cnt_r, cnt_t, cnt_b):
        print(i + 1)
        break
else:
    print(-1)