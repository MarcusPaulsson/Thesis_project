d = int(input())
n, m = map(int, input().split())

sofas = [tuple(map(int, input().split())) for _ in range(d)]

cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

def count_relation(sofa, sofas):
    (x1, y1, x2, y2) = sofa
    left = right = top = bottom = 0
    
    for (a1, a2, b1, b2) in sofas:
        if (a1, a2) != (x1, y1) and (a1, a2) != (x2, y2) and (b1, b2) != (x1, y1) and (b1, b2) != (x2, y2):
            if a1 == b1:  # Same vertical line
                if a2 < b2:
                    left += 1
                else:
                    right += 1
            elif a2 == b2:  # Same horizontal line
                if a1 < b1:
                    top += 1
                else:
                    bottom += 1

    return left, right, top, bottom

for i in range(d):
    left, right, top, bottom = count_relation(sofas[i], sofas)
    if (left, right, top, bottom) == (cnt_l, cnt_r, cnt_t, cnt_b):
        print(i + 1)
        break
else:
    print(-1)