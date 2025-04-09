def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        sofas.append(list(map(int, input().split())))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def count_left(sofa_idx):
        count = 0
        for i in range(d):
            if i != sofa_idx:
                x1_a, y1_a, x2_a, y2_a = sofas[sofa_idx]
                x1_b, y1_b, x2_b, y2_b = sofas[i]
                
                min_x_a = min(y1_a, y2_a)
                min_x_b = min(y1_b, y2_b)

                if min_x_a > min_x_b:
                    count += 1
        return count

    def count_right(sofa_idx):
        count = 0
        for i in range(d):
            if i != sofa_idx:
                x1_a, y1_a, x2_a, y2_a = sofas[sofa_idx]
                x1_b, y1_b, x2_b, y2_b = sofas[i]
                
                max_x_a = max(y1_a, y2_a)
                max_x_b = max(y1_b, y2_b)

                if max_x_a < max_x_b:
                    count += 1
        return count

    def count_top(sofa_idx):
        count = 0
        for i in range(d):
            if i != sofa_idx:
                x1_a, y1_a, x2_a, y2_a = sofas[sofa_idx]
                x1_b, y1_b, x2_b, y2_b = sofas[i]
                
                min_y_a = min(x1_a, x2_a)
                min_y_b = min(x1_b, x2_b)

                if min_y_a > min_y_b:
                    count += 1
        return count

    def count_bottom(sofa_idx):
        count = 0
        for i in range(d):
            if i != sofa_idx:
                x1_a, y1_a, x2_a, y2_a = sofas[sofa_idx]
                x1_b, y1_b, x2_b, y2_b = sofas[i]
                
                max_y_a = max(x1_a, x2_a)
                max_y_b = max(x1_b, x2_b)

                if max_y_a < max_y_b:
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