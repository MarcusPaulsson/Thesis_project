def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().split())
        sofas.append(((x1, y1), (x2, y2)))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())
    
    def count_left(sofa_index):
        count = 0
        for i in range(d):
            if i != sofa_index:
                x1_a, y1_a = sofas[sofa_index][0]
                x2_a, y2_a = sofas[sofa_index][1]
                
                x1_b, y1_b = sofas[i][0]
                x2_b, y2_b = sofas[i][1]
                
                min_y_a = min(y1_a, y2_a)
                max_y_a = max(y1_a, y2_a)
                
                min_y_b = min(y1_b, y2_b)
                max_y_b = max(y1_b, y2_b)
                
                min_x_a = min(x1_a, x2_a)
                max_x_a = max(x1_a, x2_a)
                
                min_x_b = min(x1_b, x2_b)
                max_x_b = max(x1_b, x2_b)
                
                left = False
                for x_a in [x1_a, x2_a]:
                    for y_a in [y1_a, y2_a]:
                        for x_b in [x1_b, x2_b]:
                            for y_b in [y1_b, y2_b]:
                                if x_a < x_b:
                                    left = True
                                    break
                            if left:
                                break
                        if left:
                            break
                    if left:
                        break
                
                if left:
                    count += 1
        return count
    
    def count_right(sofa_index):
        count = 0
        for i in range(d):
            if i != sofa_index:
                x1_a, y1_a = sofas[sofa_index][0]
                x2_a, y2_a = sofas[sofa_index][1]
                
                x1_b, y1_b = sofas[i][0]
                x2_b, y2_b = sofas[i][1]
                
                right = False
                for x_a in [x1_a, x2_a]:
                    for y_a in [y1_a, y2_a]:
                        for x_b in [x1_b, x2_b]:
                            for y_b in [y1_b, y2_b]:
                                if x_a > x_b:
                                    right = True
                                    break
                            if right:
                                break
                        if right:
                            break
                    if right:
                        break
                
                if right:
                    count += 1
        return count
    
    def count_top(sofa_index):
        count = 0
        for i in range(d):
            if i != sofa_index:
                x1_a, y1_a = sofas[sofa_index][0]
                x2_a, y2_a = sofas[sofa_index][1]
                
                x1_b, y1_b = sofas[i][0]
                x2_b, y2_b = sofas[i][1]
                
                top = False
                for x_a in [x1_a, x2_a]:
                    for y_a in [y1_a, y2_a]:
                        for x_b in [x1_b, x2_b]:
                            for y_b in [y1_b, y2_b]:
                                if y_a < y_b:
                                    top = True
                                    break
                            if top:
                                break
                        if top:
                            break
                    if top:
                        break
                
                if top:
                    count += 1
        return count
    
    def count_bottom(sofa_index):
        count = 0
        for i in range(d):
            if i != sofa_index:
                x1_a, y1_a = sofas[sofa_index][0]
                x2_a, y2_a = sofas[sofa_index][1]
                
                x1_b, y1_b = sofas[i][0]
                x2_b, y2_b = sofas[i][1]
                
                bottom = False
                for x_a in [x1_a, x2_a]:
                    for y_a in [y1_a, y2_a]:
                        for x_b in [x1_b, x2_b]:
                            for y_b in [y1_b, y2_b]:
                                if y_a > y_b:
                                    bottom = True
                                    break
                            if bottom:
                                break
                        if bottom:
                            break
                    if bottom:
                        break
                
                if bottom:
                    count += 1
        return count
    
    result = -1
    for i in range(d):
        l = count_left(i)
        r = count_right(i)
        t = count_top(i)
        b = count_bottom(i)
        
        if l == cnt_l and r == cnt_r and t == cnt_t and b == cnt_b:
            result = i + 1
            break
            
    print(result)

solve()