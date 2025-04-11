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
        for i in range(d):
            if i == sofa_index:
                continue
            ox1, oy1, ox2, oy2 = sofas[i]
            
            min_x = min(x1, x2)
            min_ox = min(ox1, ox2)
            
            if min_ox < min_x:
                count += 1
        return count

    def count_right(sofa_index):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_index]
        for i in range(d):
            if i == sofa_index:
                continue
            ox1, oy1, ox2, oy2 = sofas[i]
            
            max_x = max(x1, x2)
            max_ox = max(ox1, ox2)
            
            if max_ox > max_x:
                count += 1
        return count

    def count_top(sofa_index):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_index]
        for i in range(d):
            if i == sofa_index:
                continue
            ox1, oy1, ox2, oy2 = sofas[i]
            
            min_y = min(y1, y2)
            min_oy = min(oy1, oy2)
            
            if min_oy < min_y:
                count += 1
        return count

    def count_bottom(sofa_index):
        count = 0
        x1, y1, x2, y2 = sofas[sofa_index]
        for i in range(d):
            if i == sofa_index:
                continue
            ox1, oy1, ox2, oy2 = sofas[i]
            
            max_y = max(y1, y2)
            max_oy = max(oy1, oy2)
            
            if max_oy > max_y:
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