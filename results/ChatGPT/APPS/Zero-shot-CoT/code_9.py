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
        if x1 == x2:  # vertical sofa
            if y2 < oy1:  # sofa is to the top
                top += 1
            elif oy2 < y1:  # sofa is to the bottom
                bottom += 1
        else:  # horizontal sofa
            if x2 < ox1:  # sofa is to the left
                left += 1
            elif ox2 < x1:  # sofa is to the right
                right += 1

    return left, right, top, bottom

for i in range(d):
    left, right, top, bottom = count_sofas(sofas[i], sofas)
    if (left == cnt_l and right == cnt_r and top == cnt_t and bottom == cnt_b):
        print(i + 1)
        break
else:
    print(-1)