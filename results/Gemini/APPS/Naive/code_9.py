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
            x1_other, y1_other, x2_other, y2_other = sofas[i]
            min_x_other = min(x1_other, x2_other)
            min_y_other = min(y1_other, y2_other)
            max_y_other = max(y1_other, y2_other)

            if min_x > max(y1_other, y2_other):
                continue
            
            if min_x > min(x1_other, x2_other):
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
            x1_other, y1_other, x2_other, y2_other = sofas[i]
            max_x_other = max(x1_other, x2_other)
            min_y_other = min(y1_other, y2_other)
            max_y_other = max(y1_other, y2_other)

            if max_x < min(x1_other, x2_other):
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
            x1_other, y1_other, x2_other, y2_other = sofas[i]
            min_y_other = min(y1_other, y2_other)
            min_x_other = min(x1_other, x2_other)
            max_x_other = max(x1_other, x2_other)

            if min_y > max(x1_other, x2_other):
                continue
            
            if min_y > min(y1_other, y2_other):
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
            x1_other, y1_other, x2_other, y2_other = sofas[i]
            max_y_other = max(y1_other, y2_other)
            min_x_other = min(x1_other, x2_other)
            max_x_other = max(x1_other, x2_other)

            if max_y < min(y1_other, y2_other):
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