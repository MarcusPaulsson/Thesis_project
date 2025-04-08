def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().split())
        sofas.append(((x1, y1), (x2, y2)))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def count_left(sofa_index):
        count = 0
        (x1, y1), (x2, y2) = sofas[sofa_index]
        min_x = min(x1, x2)
        for i in range(d):
            if i == sofa_index:
                continue
            (ox1, oy1), (ox2, oy2) = sofas[i]
            max_x_other = max(ox1, ox2)
            if min_x > max_x_other:
                count += 1
        return count

    def count_right(sofa_index):
        count = 0
        (x1, y1), (x2, y2) = sofas[sofa_index]
        max_x = max(x1, x2)
        for i in range(d):
            if i == sofa_index:
                continue
            (ox1, oy1), (ox2, oy2) = sofas[i]
            min_x_other = min(ox1, ox2)
            if max_x < min_x_other:
                count += 1
        return count

    def count_top(sofa_index):
        count = 0
        (x1, y1), (x2, y2) = sofas[sofa_index]
        min_y = min(y1, y2)
        for i in range(d):
            if i == sofa_index:
                continue
            (ox1, oy1), (ox2, oy2) = sofas[i]
            max_y_other = max(oy1, oy2)
            if min_y > max_y_other:
                count += 1
        return count

    def count_bottom(sofa_index):
        count = 0
        (x1, y1), (x2, y2) = sofas[sofa_index]
        max_y = max(y1, y2)
        for i in range(d):
            if i == sofa_index:
                continue
            (ox1, oy1), (ox2, oy2) = sofas[i]
            min_y_other = min(oy1, oy2)
            if max_y < min_y_other:
                count += 1
        return count

    for i in range(d):
        if (count_left(i) == cnt_l and
            count_right(i) == cnt_r and
            count_top(i) == cnt_t and
            count_bottom(i) == cnt_b):
            print(i + 1)
            return

    print(-1)

solve()