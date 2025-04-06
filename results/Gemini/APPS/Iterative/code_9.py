def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().split())
        sofas.append(((x1, y1), (x2, y2)))
    
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())
    
    def count_left(sofa_idx):
        count = 0
        s1, s2 = sofas[sofa_idx]
        min_x = min(s1[0], s2[0])
        max_x = max(s1[0], s2[0])
        min_y = min(s1[1], s2[1])
        max_y = max(s1[1], s2[1])

        for i in range(d):
            if i != sofa_idx:
                o1, o2 = sofas[i]
                omin_x = min(o1[0], o2[0])
                omax_x = max(o1[0], o2[0])
                omin_y = min(o1[1], o2[1])
                omax_y = max(o1[1], o2[1])

                if max_y < omin_y:
                    count += 1
        return count

    def count_right(sofa_idx):
        count = 0
        s1, s2 = sofas[sofa_idx]
        min_x = min(s1[0], s2[0])
        max_x = max(s1[0], s2[0])
        min_y = min(s1[1], s2[1])
        max_y = max(s1[1], s2[1])

        for i in range(d):
            if i != sofa_idx:
                o1, o2 = sofas[i]
                omin_x = min(o1[0], o2[0])
                omax_x = max(o1[0], o2[0])
                omin_y = min(o1[1], o2[1])
                omax_y = max(o1[1], o2[1])
                
                if min_y > omax_y:
                    count += 1
        return count

    def count_top(sofa_idx):
        count = 0
        s1, s2 = sofas[sofa_idx]
        min_x = min(s1[0], s2[0])
        max_x = max(s1[0], s2[0])
        min_y = min(s1[1], s2[1])
        max_y = max(s1[1], s2[1])
        
        for i in range(d):
            if i != sofa_idx:
                o1, o2 = sofas[i]
                omin_x = min(o1[0], o2[0])
                omax_x = max(o1[0], o2[0])
                omin_y = min(o1[1], o2[1])
                omax_y = max(o1[1], o2[1])
                
                if max_x < omin_x:
                    count += 1
        return count

    def count_bottom(sofa_idx):
        count = 0
        s1, s2 = sofas[sofa_idx]
        min_x = min(s1[0], s2[0])
        max_x = max(s1[0], s2[0])
        min_y = min(s1[1], s2[1])
        max_y = max(s1[1], s2[1])
        
        for i in range(d):
            if i != sofa_idx:
                o1, o2 = sofas[i]
                omin_x = min(o1[0], o2[0])
                omax_x = max(o1[0], o2[0])
                omin_y = min(o1[1], o2[1])
                omax_y = max(o1[1], o2[1])
                
                if min_x > omax_x:
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