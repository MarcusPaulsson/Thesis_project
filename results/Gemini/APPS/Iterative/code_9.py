def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().split())
        sofas.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def check_sofa(sofa_index):
        l = 0
        r = 0
        t = 0
        b = 0
        
        x1, y1, x2, y2 = sofas[sofa_index]
        
        for i in range(d):
            if i == sofa_index:
                continue
            
            ox1, oy1, ox2, oy2 = sofas[i]
            
            # Check left
            if x1 > ox2:
                l += 1
            # Check right
            if x2 < ox1:
                r += 1
            # Check top
            if y1 > oy2:
                t += 1
            # Check bottom
            if y2 < oy1:
                b += 1
                
        return l == cnt_l and r == cnt_r and t == cnt_t and b == cnt_b

    result = -1
    for i in range(d):
        if check_sofa(i):
            result = i + 1
            break

    print(result)

solve()