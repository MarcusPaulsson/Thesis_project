def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        sofas.append(list(map(int, input().split())))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def count_left(sofa, all_sofas):
        count = 0
        x1, y1, x2, y2 = sofa
        min_x = min(x1, x2)
        for other_sofa in all_sofas:
            if sofa == other_sofa:
                continue
            ox1, oy1, ox2, oy2 = other_sofa
            min_ox = min(ox1, ox2)
            if min_ox < min_x:
                count += 1
        return count

    def count_right(sofa, all_sofas):
        count = 0
        x1, y1, x2, y2 = sofa
        max_x = max(x1, x2)
        for other_sofa in all_sofas:
            if sofa == other_sofa:
                continue
            ox1, oy1, ox2, oy2 = other_sofa
            max_ox = max(ox1, ox2)
            if max_ox > max_x:
                count += 1
        return count

    def count_top(sofa, all_sofas):
        count = 0
        x1, y1, x2, y2 = sofa
        min_y = min(y1, y2)
        for other_sofa in all_sofas:
            if sofa == other_sofa:
                continue
            ox1, oy1, ox2, oy2 = other_sofa
            min_oy = min(oy1, oy2)
            if min_oy < min_y:
                count += 1
        return count

    def count_bottom(sofa, all_sofas):
        count = 0
        x1, y1, x2, y2 = sofa
        max_y = max(y1, y2)
        for other_sofa in all_sofas:
            if sofa == other_sofa:
                continue
            ox1, oy1, ox2, oy2 = other_sofa
            max_oy = max(oy1, oy2)
            if max_oy > max_y:
                count += 1
        return count

    result = -1
    for i in range(d):
        sofa = sofas[i]
        
        l = count_left(sofa, sofas)
        r = count_right(sofa, sofas)
        t = count_top(sofa, sofas)
        b = count_bottom(sofa, sofas)

        if l == cnt_l and r == cnt_r and t == cnt_t and b == cnt_b:
            result = i + 1
            break

    print(result)

solve()