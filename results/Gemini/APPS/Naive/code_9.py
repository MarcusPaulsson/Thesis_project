def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        sofas.append(list(map(int, input().split())))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def count_sofas(sofa_index):
        l, r, t, b = 0, 0, 0, 0
        x1_s, y1_s, x2_s, y2_s = sofas[sofa_index]

        for i in range(d):
            if i == sofa_index:
                continue

            x1_o, y1_o, x2_o, y2_o = sofas[i]

            # Check left
            if min(x1_s, x2_s) > max(x1_o, x2_o):
                l += 1
            # Check right
            if max(x1_s, x2_s) < min(x1_o, x2_o):
                r += 1
            # Check top
            if min(y1_s, y2_s) > max(y1_o, y2_o):
                t += 1
            # Check bottom
            if max(y1_s, y2_s) < min(y1_o, y2_o):
                b += 1

        return l, r, t, b

    for i in range(d):
        l, r, t, b = count_sofas(i)
        if l == cnt_l and r == cnt_r and t == cnt_t and b == cnt_b:
            print(i + 1)
            return

    print(-1)

solve()