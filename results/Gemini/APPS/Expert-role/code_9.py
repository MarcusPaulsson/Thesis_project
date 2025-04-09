def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        sofas.append(list(map(int, input().split())))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def count_sofas(sofa_index):
        l, r, t, b = 0, 0, 0, 0
        x1_a, y1_a, x2_a, y2_a = sofas[sofa_index]

        for i in range(d):
            if i == sofa_index:
                continue
            x1_b, y1_b, x2_b, y2_b = sofas[i]

            # Check left
            if min(y1_a, y2_a) > max(y1_b, y2_b):
                continue
            if max(y1_a, y2_a) < min(y1_b, y2_b):
                continue

            if min(x1_a, x2_a) > max(x1_b, x2_b):
                l += 1
            
            # Check right
            if min(y1_a, y2_a) > max(y1_b, y2_b):
                continue
            if max(y1_a, y2_a) < min(y1_b, y2_b):
                continue
            if max(x1_a, x2_a) < min(x1_b, x2_b):
                r += 1
            
            # Check top
            if min(x1_a, x2_a) > max(x1_b, x2_b):
                continue
            if max(x1_a, x2_a) < min(x1_b, x2_b):
                continue
                
            if min(y1_a, y2_a) > max(y1_b, y2_b):
                t += 1

            # Check bottom
            if min(x1_a, x2_a) > max(x1_b, x2_b):
                continue
            if max(x1_a, x2_a) < min(x1_b, x2_b):
                continue
                
            if max(y1_a, y2_a) < min(y1_b, y2_b):
                b += 1
        return l, r, t, b

    result = -1
    for i in range(d):
        l, r, t, b = count_sofas(i)
        if l == cnt_l and r == cnt_r and t == cnt_t and b == cnt_b:
            result = i + 1
            break

    print(result)

solve()