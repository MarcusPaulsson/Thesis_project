def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        sofas.append(list(map(int, input().split())))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def count_left(sofa_index):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_index]
        left_most = min(y1, y2)
        for i in range(d):
            if i == sofa_index:
                continue
            x1_other, y1_other, x2_other, y2_other = sofas[i]
            right_most_other = max(y1_other, y2_other)
            if right_most_other < left_most:
                count += 1
        return count

    def count_right(sofa_index):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_index]
        right_most = max(y1, y2)
        for i in range(d):
            if i == sofa_index:
                continue
            x1_other, y1_other, x2_other, y2_other = sofas[i]
            left_most_other = min(y1_other, y2_other)
            if left_most_other > right_most:
                count += 1
        return count

    def count_top(sofa_index):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_index]
        top_most = min(x1, x2)
        for i in range(d):
            if i == sofa_index:
                continue
            x1_other, y1_other, x2_other, y2_other = sofas[i]
            bottom_most_other = max(x1_other, x2_other)
            if bottom_most_other < top_most:
                count += 1
        return count

    def count_bottom(sofa_index):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_index]
        bottom_most = max(x1, x2)
        for i in range(d):
            if i == sofa_index:
                continue
            x1_other, y1_other, x2_other, y2_other = sofas[i]
            top_most_other = min(x1_other, x2_other)
            if top_most_other > bottom_most:
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