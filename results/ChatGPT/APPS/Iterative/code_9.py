d = int(input())
n, m = map(int, input().split())
sofas = []

for _ in range(d):
    x1, y1, x2, y2 = map(int, input().split())
    sofas.append((x1, y1, x2, y2))

cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

def count_sofas(sofa_index):
    x1, y1, x2, y2 = sofas[sofa_index]
    left_count = right_count = top_count = bottom_count = 0

    for i in range(d):
        if i == sofa_index:
            continue
        sx1, sy1, sx2, sy2 = sofas[i]
        
        if (x2 < sx1):  # Current sofa is to the left
            left_count += 1
        elif (x1 > sx2):  # Current sofa is to the right
            right_count += 1
        if (y2 < sy1):  # Current sofa is above
            top_count += 1
        elif (y1 > sy2):  # Current sofa is below
            bottom_count += 1

    return left_count, right_count, top_count, bottom_count

for i in range(d):
    left, right, top, bottom = count_sofas(i)
    if left == cnt_l and right == cnt_r and top == cnt_t and bottom == cnt_b:
        print(i + 1)
        break
else:
    print(-1)