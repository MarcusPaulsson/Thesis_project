def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().split())
        sofas.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def check_conditions(sofa_index):
        l_count = 0
        r_count = 0
        t_count = 0
        b_count = 0

        target_sofa = sofas[sofa_index]
        target_x1, target_y1, target_x2, target_y2 = target_sofa

        for i in range(d):
            if i == sofa_index:
                continue

            other_sofa = sofas[i]
            other_x1, other_y1, other_x2, other_y2 = other_sofa

            if target_y2 < other_y1:
                l_count += 1
            elif target_y1 > other_y2:
                r_count += 1
            if target_x2 < other_x1:
                t_count += 1
            elif target_x1 > other_x2:
                b_count += 1

        return l_count == cnt_l and r_count == cnt_r and t_count == cnt_t and b_count == cnt_b

    result = -1
    for i in range(d):
        if check_conditions(i):
            result = i + 1
            break

    print(result)

solve()