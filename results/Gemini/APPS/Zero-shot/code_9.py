def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().split())
        sofas.append((x1, y1, x2, y2))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    for i in range(d):
        l, r, t, b = 0, 0, 0, 0
        for j in range(d):
            if i == j:
                continue

            x1_i, y1_i, x2_i, y2_i = sofas[i]
            x1_j, y1_j, x2_j, y2_j = sofas[j]

            min_x_i = min(y1_i, y2_i)
            max_x_i = max(y1_i, y2_i)
            min_y_i = min(x1_i, x2_i)
            max_y_i = max(x1_i, x2_i)
            
            min_x_j = min(y1_j, y2_j)
            max_x_j = max(y1_j, y2_j)
            min_y_j = min(x1_j, x2_j)
            max_y_j = max(x1_j, x2_j)
            
            
            
            is_left = False
            is_right = False
            is_top = False
            is_bottom = False
            
            if min_x_i > max_x_j:
                is_left = True
            if max_x_i < min_x_j:
                is_right = True
            if min_y_i > max_y_j:
                is_top = True
            if max_y_i < min_y_j:
                is_bottom = True

            if is_left:
                l += 1
            if is_right:
                r += 1
            if is_top:
                t += 1
            if is_bottom:
                b += 1

        if l == cnt_l and r == cnt_r and t == cnt_t and b == cnt_b:
            print(i + 1)
            return

    print(-1)

solve()