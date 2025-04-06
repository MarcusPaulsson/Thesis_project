def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        sofas.append(list(map(int, input().split())))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def count_left(sofa, sofas_list):
        count = 0
        x1, y1, x2, y2 = sofa
        min_x = min(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)

        for other_sofa in sofas_list:
            if sofa == other_sofa:
                continue
            ox1, oy1, ox2, oy2 = other_sofa
            other_min_x = min(ox1, ox2)
            
            if other_min_x < min_x:
                count += 1
        return count

    def count_right(sofa, sofas_list):
        count = 0
        x1, y1, x2, y2 = sofa
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)

        for other_sofa in sofas_list:
            if sofa == other_sofa:
                continue
            ox1, oy1, ox2, oy2 = other_sofa
            other_max_x = max(ox1, ox2)

            if other_max_x > max_x:
                count += 1
        return count

    def count_top(sofa, sofas_list):
        count = 0
        x1, y1, x2, y2 = sofa
        min_y = min(y1, y2)
        min_x = min(x1, x2)
        max_x = max(x1, x2)

        for other_sofa in sofas_list:
            if sofa == other_sofa:
                continue
            ox1, oy1, ox2, oy2 = other_sofa
            other_min_y = min(oy1, oy2)

            if other_min_y < min_y:
                count += 1
        return count

    def count_bottom(sofa, sofas_list):
        count = 0
        x1, y1, x2, y2 = sofa
        max_y = max(y1, y2)
        min_x = min(x1, x2)
        max_x = max(x1, x2)

        for other_sofa in sofas_list:
            if sofa == other_sofa:
                continue
            ox1, oy1, ox2, oy2 = other_sofa
            other_max_y = max(oy1, oy2)

            if other_max_y > max_y:
                count += 1
        return count

    result = -1
    for i in range(d):
        left_count = count_left(sofas[i], sofas)
        right_count = count_right(sofas[i], sofas)
        top_count = count_top(sofas[i], sofas)
        bottom_count = count_bottom(sofas[i], sofas)

        if (left_count == cnt_l and
            right_count == cnt_r and
            top_count == cnt_t and
            bottom_count == cnt_b):
            result = i + 1
            break

    print(result)

solve()