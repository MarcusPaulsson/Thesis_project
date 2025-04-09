def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().split())
        sofas.append((x1, y1, x2, y2))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def count_left(sofa_index):
        count = 0
        x1_a, y1_a, x2_a, y2_a = sofas[sofa_index]
        min_x_a = min(x1_a, x2_a)

        for i in range(d):
            if i != sofa_index:
                x1_b, y1_b, x2_b, y2_b = sofas[i]
                min_x_b = min(x1_b, x2_b)

                if min_x_a > min_x_b:
                    count += 1
        return count

    def count_right(sofa_index):
        count = 0
        x1_a, y1_a, x2_a, y2_a = sofas[sofa_index]
        max_x_a = max(x1_a, x2_a)
        
        for i in range(d):
            if i != sofa_index:
                x1_b, y1_b, x2_b, y2_b = sofas[i]
                max_x_b = max(x1_b, x2_b)

                if max_x_a < max_x_b:
                    count += 1
        return count

    def count_top(sofa_index):
        count = 0
        x1_a, y1_a, x2_a, y2_a = sofas[sofa_index]
        min_y_a = min(y1_a, y2_a)

        for i in range(d):
            if i != sofa_index:
                x1_b, y1_b, x2_b, y2_b = sofas[i]
                min_y_b = min(y1_b, y2_b)

                if min_y_a > min_y_b:
                    count += 1
        return count

    def count_bottom(sofa_index):
        count = 0
        x1_a, y1_a, x2_a, y2_a = sofas[sofa_index]
        max_y_a = max(y1_a, y2_a)

        for i in range(d):
            if i != sofa_index:
                x1_b, y1_b, x2_b, y2_b = sofas[i]
                max_y_b = max(y1_b, y2_b)

                if max_y_a < max_y_b:
                    count += 1
        return count

    for i in range(d):
        if (count_left(i) == cnt_l and
            count_right(i) == cnt_r and
            count_top(i) == cnt_t and
            count_bottom(i) == cnt_b):
            print(i + 1)
            return

    print("-1")

solve()