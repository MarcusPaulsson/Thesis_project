d = int(input())
n, m = map(int, input().split())
sofas = []

for i in range(d):
    x1, y1, x2, y2 = map(int, input().split())
    sofas.append((x1, y1, x2, y2))

cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

def count_sofas(sofas, x1, y1, x2, y2):
    left = right = top = bottom = 0
    for (sx1, sy1, sx2, sy2) in sofas:
        if sx1 == sx2:  # vertical sofa
            if sy1 < y1:  # sofa is to the left
                left += 1
            elif sy1 > y2:  # sofa is to the right
                right += 1
            if sx1 < x1:  # sofa is above
                top += 1
            elif sx1 > x2:  # sofa is below
                bottom += 1
        else:  # horizontal sofa
            if sx1 < x1:  # sofa is above
                top += 1
            elif sx1 > x2:  # sofa is below
                bottom += 1
            if sy1 < y1:  # sofa is to the left
                left += 1
            elif sy1 > y2:  # sofa is to the right
                right += 1
    return left, right, top, bottom

for i in range(d):
    x1, y1, x2, y2 = sofas[i]
    left, right, top, bottom = count_sofas(sofas[:i] + sofas[i+1:], x1, y1, x2, y2)
    if left == cnt_l and right == cnt_r and top == cnt_t and bottom == cnt_b:
        print(i + 1)
        break
else:
    print(-1)