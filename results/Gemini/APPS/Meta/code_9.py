def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        sofas.append(list(map(int, input().split())))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def count_sofas(sofa_index):
        l, r, t, b = 0, 0, 0, 0
        x1, y1, x2, y2 = sofas[sofa_index]
        
        for i in range(d):
            if i == sofa_index:
                continue
            
            ox1, oy1, ox2, oy2 = sofas[i]
            
            # Check left
            if min(x1, x2) > max(ox1, ox2):
                l += 1
            # Check right
            if max(x1, x2) < min(ox1, ox2):
                r += 1
            # Check top
            if min(y1, y2) > max(oy1, oy2):
                t += 1
            # Check bottom
            if max(y1, y2) < min(oy1, oy2):
                b += 1
        return l, r, t, b

    for i in range(d):
        l, r, t, b = count_sofas(i)
        if l == cnt_l and r == cnt_r and t == cnt_t and b == cnt_b:
            print(i + 1)
            return

    print(-1)

solve()