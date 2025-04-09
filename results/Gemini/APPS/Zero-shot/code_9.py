def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        sofas.append(list(map(int, input().split())))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def count_left(sofa, other_sofas):
        count = 0
        for other_sofa in other_sofas:
            if sofa == other_sofa:
                continue
            
            x1_sofa = min(sofa[0], sofa[2])
            x2_sofa = max(sofa[0], sofa[2])
            y1_sofa = min(sofa[1], sofa[3])
            y2_sofa = max(sofa[1], sofa[3])

            x1_other = min(other_sofa[0], other_sofa[2])
            x2_other = max(other_sofa[0], other_sofa[2])
            y1_other = min(other_sofa[1], other_sofa[3])
            y2_other = max(other_sofa[1], other_sofa[3])
            
            
            min_x_sofa = min(sofa[0], sofa[2])
            min_x_other = min(other_sofa[0], other_sofa[2])
        
            if min_x_sofa > x1_other:
                count += 1
        return count

    def count_right(sofa, other_sofas):
        count = 0
        for other_sofa in other_sofas:
            if sofa == other_sofa:
                continue

            
            x1_sofa = min(sofa[0], sofa[2])
            x2_sofa = max(sofa[0], sofa[2])
            y1_sofa = min(sofa[1], sofa[3])
            y2_sofa = max(sofa[1], sofa[3])

            x1_other = min(other_sofa[0], other_sofa[2])
            x2_other = max(other_sofa[0], other_sofa[2])
            y1_other = min(other_sofa[1], other_sofa[3])
            y2_other = max(other_sofa[1], other_sofa[3])
            
            max_x_sofa = max(sofa[0], sofa[2])
            max_x_other = max(other_sofa[0], other_sofa[2])
            
            if max_x_sofa < x2_other:
                count += 1
        return count

    def count_top(sofa, other_sofas):
        count = 0
        for other_sofa in other_sofas:
            if sofa == other_sofa:
                continue

            x1_sofa = min(sofa[0], sofa[2])
            x2_sofa = max(sofa[0], sofa[2])
            y1_sofa = min(sofa[1], sofa[3])
            y2_sofa = max(sofa[1], sofa[3])

            x1_other = min(other_sofa[0], other_sofa[2])
            x2_other = max(other_sofa[0], other_sofa[2])
            y1_other = min(other_sofa[1], other_sofa[3])
            y2_other = max(other_sofa[1], other_sofa[3])
            
            min_y_sofa = min(sofa[1], sofa[3])
            min_y_other = min(other_sofa[1], other_sofa[3])
            
            if min_y_sofa > y1_other:
                count += 1
        return count

    def count_bottom(sofa, other_sofas):
        count = 0
        for other_sofa in other_sofas:
            if sofa == other_sofa:
                continue
            
            x1_sofa = min(sofa[0], sofa[2])
            x2_sofa = max(sofa[0], sofa[2])
            y1_sofa = min(sofa[1], sofa[3])
            y2_sofa = max(sofa[1], sofa[3])

            x1_other = min(other_sofa[0], other_sofa[2])
            x2_other = max(other_sofa[0], other_sofa[2])
            y1_other = min(other_sofa[1], other_sofa[3])
            y2_other = max(other_sofa[1], other_sofa[3])
            
            max_y_sofa = max(sofa[1], sofa[3])
            max_y_other = max(other_sofa[1], other_sofa[3])

            if max_y_sofa < y2_other:
                count += 1
        return count

    for i in range(d):
        sofa = sofas[i]
        other_sofas = sofas[:]
        
        
        l = count_left(sofa, other_sofas)
        r = count_right(sofa, other_sofas)
        t = count_top(sofa, other_sofas)
        b = count_bottom(sofa, other_sofas)

        if l == cnt_l and r == cnt_r and t == cnt_t and b == cnt_b:
            print(i + 1)
            return

    print(-1)

solve()