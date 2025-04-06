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
        min_y_a = min(y1_a, y2_a)
        for i in range(d):
            if i != sofa_index:
                x1_b, y1_b, x2_b, y2_b = sofas[i]
                min_y_b = min(y1_b, y2_b)
                if min(x1_a, x2_a) > max(x1_b, x2_b):
                    count += 0
                elif max(x1_a,x2_a) < min(x1_b,x2_b):
                    count += 0
                elif min_y_a > min_y_b:
                    count += 0
                elif max(y1_a, y2_a) < min(y1_b, y2_b):
                    count += 0
                else:
                    
                    overlap = False
                    
                    if (x1_a == x2_a and x1_b == x2_b):
                        if x1_a == x1_b:
                            if max(y1_a, y2_a) >= min(y1_b, y2_b) and min(y1_a, y2_a) <= max(y1_b, y2_b):
                                overlap = True
                    
                    if (y1_a == y2_a and y1_b == y2_b):
                        if y1_a == y1_b:
                            if max(x1_a, x2_a) >= min(x1_b, x2_b) and min(x1_a, x2_a) <= max(x1_b, x2_b):
                                overlap = True
                                
                    if (x1_a < x1_b) and not overlap:
                        count += 1
                        
        return count

    def count_right(sofa_index):
        count = 0
        x1_a, y1_a, x2_a, y2_a = sofas[sofa_index]
        min_y_a = min(y1_a, y2_a)
        for i in range(d):
            if i != sofa_index:
                x1_b, y1_b, x2_b, y2_b = sofas[i]
                min_y_b = min(y1_b, y2_b)
                if min(x1_a, x2_a) > max(x1_b, x2_b):
                    count += 0
                elif max(x1_a,x2_a) < min(x1_b,x2_b):
                    count += 0
                elif min_y_a > min_y_b:
                    count += 0
                elif max(y1_a, y2_a) < min(y1_b, y2_b):
                    count += 0
                else:
                    
                    overlap = False
                    
                    if (x1_a == x2_a and x1_b == x2_b):
                        if x1_a == x1_b:
                            if max(y1_a, y2_a) >= min(y1_b, y2_b) and min(y1_a, y2_a) <= max(y1_b, y2_b):
                                overlap = True
                    
                    if (y1_a == y2_a and y1_b == y2_b):
                        if y1_a == y1_b:
                            if max(x1_a, x2_a) >= min(x1_b, x2_b) and min(x1_a, x2_a) <= max(x1_b, x2_b):
                                overlap = True
                                
                    if (x1_a > x1_b) and not overlap:
                        count += 1
        return count

    def count_top(sofa_index):
        count = 0
        x1_a, y1_a, x2_a, y2_a = sofas[sofa_index]
        min_x_a = min(x1_a,x2_a)
        for i in range(d):
            if i != sofa_index:
                x1_b, y1_b, x2_b, y2_b = sofas[i]
                min_x_b = min(x1_b,x2_b)
                if min(y1_a, y2_a) > max(y1_b, y2_b):
                    count += 0
                elif max(y1_a,y2_a) < min(y1_b,y2_b):
                    count += 0
                elif min_x_a > min_x_b:
                    count += 0
                elif max(x1_a, x2_a) < min(x1_b, x2_b):
                    count += 0
                else:
                    overlap = False
                    
                    if (x1_a == x2_a and x1_b == x2_b):
                        if x1_a == x1_b:
                            if max(y1_a, y2_a) >= min(y1_b, y2_b) and min(y1_a, y2_a) <= max(y1_b, y2_b):
                                overlap = True
                    
                    if (y1_a == y2_a and y1_b == y2_b):
                        if y1_a == y1_b:
                            if max(x1_a, x2_a) >= min(x1_b, x2_b) and min(x1_a, x2_a) <= max(x1_b, x2_b):
                                overlap = True
                                
                    if (y1_a < y1_b) and not overlap:
                        count += 1
        return count

    def count_bottom(sofa_index):
        count = 0
        x1_a, y1_a, x2_a, y2_a = sofas[sofa_index]
        min_x_a = min(x1_a,x2_a)
        for i in range(d):
            if i != sofa_index:
                x1_b, y1_b, x2_b, y2_b = sofas[i]
                min_x_b = min(x1_b,x2_b)
                if min(y1_a, y2_a) > max(y1_b, y2_b):
                    count += 0
                elif max(y1_a,y2_a) < min(y1_b,y2_b):
                    count += 0
                elif min_x_a > min_x_b:
                    count += 0
                elif max(x1_a, x2_a) < min(x1_b, x2_b):
                    count += 0
                else:
                    overlap = False
                    
                    if (x1_a == x2_a and x1_b == x2_b):
                        if x1_a == x1_b:
                            if max(y1_a, y2_a) >= min(y1_b, y2_b) and min(y1_a, y2_a) <= max(y1_b, y2_b):
                                overlap = True
                    
                    if (y1_a == y2_a and y1_b == y2_b):
                        if y1_a == y1_b:
                            if max(x1_a, x2_a) >= min(x1_b, x2_b) and min(x1_a, x2_a) <= max(x1_b, x2_b):
                                overlap = True
                                
                    if (y1_a > y1_b) and not overlap:
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