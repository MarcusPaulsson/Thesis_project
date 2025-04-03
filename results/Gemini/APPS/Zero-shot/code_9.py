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
        min_x = min(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        for i in range(d):
            if i == sofa_index:
                continue
            ox1, oy1, ox2, oy2 = sofas[i]
            omin_x = min(ox1, ox2)
            omin_y = min(oy1, oy2)
            omax_y = max(oy1, oy2)
            if omin_x < min_x:
                count += 1
        return count

    def count_right(sofa_index):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_index]
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        for i in range(d):
            if i == sofa_index:
                continue
            ox1, oy1, ox2, oy2 = sofas[i]
            omax_x = max(ox1, ox2)
            omin_y = min(oy1, oy2)
            omax_y = max(oy1, oy2)
            if omax_x > max_x:
                count += 1
        return count

    def count_top(sofa_index):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_index]
        min_y = min(y1, y2)
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        for i in range(d):
            if i == sofa_index:
                continue
            ox1, oy1, ox2, oy2 = sofas[i]
            omin_y = min(oy1, oy2)
            omin_x = min(ox1, ox2)
            omax_x = max(ox1, ox2)
            if omin_y < min_y:
                count += 1
        return count

    def count_bottom(sofa_index):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_index]
        max_y = max(y1, y2)
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        for i in range(d):
            if i == sofa_index:
                continue
            ox1, oy1, ox2, oy2 = sofas[i]
            omax_y = max(oy1, oy2)
            omin_x = min(ox1, ox2)
            omax_x = max(ox1, ox2)
            if omax_y > max_y:
                count += 1
        return count

    result = -1
    for i in range(d):
        l = count_left(i)
        r = count_right(i)
        t = count_top(i)
        b = count_bottom(i)
        if l == cnt_l and r == cnt_r and t == cnt_t and b == cnt_b:
            result = i + 1
            break

    print(result)

solve()