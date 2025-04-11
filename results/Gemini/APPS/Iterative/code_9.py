def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().split())
        sofas.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def count_left(sofa_idx):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_idx]
        for i in range(d):
            if i == sofa_idx:
                continue
            x1_other, y1_other, x2_other, y2_other = sofas[i]
            if y1_other <= y2 and y2_other >= y1:
                if x1_other < x2:
                    count += 1
        return count

    def count_right(sofa_idx):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_idx]
        for i in range(d):
            if i == sofa_idx:
                continue
            x1_other, y1_other, x2_other, y2_other = sofas[i]
            if y1_other <= y2 and y2_other >= y1:
                if x2_other > x1:
                    count += 1
        return count

    def count_top(sofa_idx):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_idx]
        for i in range(d):
            if i == sofa_idx:
                continue
            x1_other, y1_other, x2_other, y2_other = sofas[i]
            if x1_other <= x2 and x2_other >= x1:
                if y1_other < y2:
                    count += 1
        return count

    def count_bottom(sofa_idx):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_idx]
        for i in range(d):
            if i == sofa_idx:
                continue
            x1_other, y1_other, x2_other, y2_other = sofas[i]
            if x1_other <= x2 and x2_other >= x1:
                if y2_other > y1:
                    count += 1
        return count

    for i in range(d):
        l = count_left(i)
        r = count_right(i)
        t = count_top(i)
        b = count_bottom(i)
        if l == cnt_l and r == cnt_r and t == cnt_t and b == cnt_b:
            print(i + 1)
            return

    print(-1)

solve()