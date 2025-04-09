d = int(input())
n, m = map(int, input().split())
sofas = []

for i in range(d):
    x1, y1, x2, y2 = map(int, input().split())
    sofas.append((x1, y1, x2, y2))

cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

def count_sofas(sofa_index):
    x1, y1, x2, y2 = sofas[sofa_index]
    left = right = top = bottom = 0
    
    for i in range(d):
        if i == sofa_index:
            continue
        x1_cmp, y1_cmp, x2_cmp, y2_cmp = sofas[i]
        if x1 == x2:  # vertical sofa
            if y1 < y1_cmp < y2:  # sofa i is to the right
                right += 1
            elif y1_cmp < y1 < y2_cmp:  # sofa i is to the left
                left += 1
        else:  # horizontal sofa
            if x1 < x1_cmp < x2:  # sofa i is below
                bottom += 1
            elif x1_cmp < x1 < x2_cmp:  # sofa i is above
                top += 1

    return left, right, top, bottom

result = -1

for i in range(d):
    left, right, top, bottom = count_sofas(i)
    if (left == cnt_l and right == cnt_r and top == cnt_t and bottom == cnt_b):
        if result == -1:
            result = i + 1  # sofas are 1-indexed
        else:
            result = -1  # more than one match found

print(result)