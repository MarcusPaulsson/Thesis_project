def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        sofas.append(list(map(int, input().split())))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def count_sofas(sofa_index):
        l, r, t, b = 0, 0, 0, 0
        x1, y1, x2, y2 = sofas[sofa_index]
        
        for i in range(d):
            if i == sofa_index:
                continue
            
            other_x1, other_y1, other_x2, other_y2 = sofas[i]
            
            # Check left
            if min(x1, x2) > max(other_x1, other_x2):
                l += 1
            elif min(x1, x2) < max(other_x1, other_x2) and max(x1,x2) > min(other_x1, other_x2):
                
                found_left = False
                
                if x1 < other_x1:
                    found_left = True
                if x1 < other_x2:
                    found_left = True
                if x2 < other_x1:
                    found_left = True
                if x2 < other_x2:
                    found_left = True
                
                if found_left:
                    l +=1
            
            # Check right
            if max(x1, x2) < min(other_x1, other_x2):
                r += 1
            elif min(x1, x2) < max(other_x1, other_x2) and max(x1,x2) > min(other_x1, other_x2):
                found_right = False

                if x1 > other_x1:
                    found_right = True
                if x1 > other_x2:
                    found_right = True
                if x2 > other_x1:
                    found_right = True
                if x2 > other_x2:
                    found_right = True
                    
                if found_right:
                    r += 1
            
            # Check top
            if min(y1, y2) > max(other_y1, other_y2):
                t += 1
            elif min(y1, y2) < max(other_y1, other_y2) and max(y1,y2) > min(other_y1, other_y2):
                
                found_top = False
                
                if y1 < other_y1:
                    found_top = True
                if y1 < other_y2:
                    found_top = True
                if y2 < other_y1:
                    found_top = True
                if y2 < other_y2:
                    found_top = True
                    
                if found_top:
                    t += 1
            
            # Check bottom
            if max(y1, y2) < min(other_y1, other_y2):
                b += 1
            elif min(y1, y2) < max(other_y1, other_y2) and max(y1,y2) > min(other_y1, other_y2):
                
                found_bottom = False
                
                if y1 > other_y1:
                    found_bottom = True
                if y1 > other_y2:
                    found_bottom = True
                if y2 > other_y1:
                    found_bottom = True
                if y2 > other_y2:
                    found_bottom = True
                if found_bottom:
                    b += 1
        
        return l, r, t, b

    result = -1
    for i in range(d):
        l, r, t, b = count_sofas(i)
        if l == cnt_l and r == cnt_r and t == cnt_t and b == cnt_b:
            result = i + 1
            break

    print(result)

solve()