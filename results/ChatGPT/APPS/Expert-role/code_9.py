d = int(input())
n, m = map(int, input().split())

sofas = []
for i in range(d):
    x1, y1, x2, y2 = map(int, input().split())
    sofas.append((x1, y1, x2, y2))

cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

def count_neighbors(sofa, sofas):
    x1, y1, x2, y2 = sofa
    left = right = top = bottom = 0
    
    for sx1, sy1, sx2, sy2 in sofas:
        if (sx1, sy1) != (x1, y1) and (sx1, sy1) != (x2, y2) and (sx2, sy2) != (x1, y1) and (sx2, sy2) != (x2, y2):
            if x1 < sx1 < x2:  # sofa is to the left
                left += 1
            if x1 > sx1 > x2:  # sofa is to the right
                right += 1
            if y1 < sy1 < y2:  # sofa is above
                top += 1
            if y1 > sy1 > y2:  # sofa is below
                bottom += 1
                
    return left, right, top, bottom

for i in range(d):
    left, right, top, bottom = count_neighbors(sofas[i], sofas)
    if (left == cnt_l and right == cnt_r and top == cnt_t and bottom == cnt_b):
        print(i + 1)
        break
else:
    print(-1)