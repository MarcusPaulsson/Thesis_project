def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        sofas.append(list(map(int, input().split())))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())
    
    def count_sofas(sofa_index):
        l, r, t, b = 0, 0, 0, 0
        x1_s, y1_s, x2_s, y2_s = sofas[sofa_index]
        
        for i in range(d):
            if i == sofa_index:
                continue
            x1, y1, x2, y2 = sofas[i]
            
            # Check left
            if min(y1_s, y2_s) > max(y1, y2):
                l_found = False
                if x1_s < x1:
                  l_found = True
                if x2_s < x1:
                  l_found = True
                if x1_s < x2:
                  l_found = True
                if x2_s < x2:
                  l_found = True
                if l_found:
                  l += 1
                  continue
                  
            if min(y1_s, y2_s) > max(y2, y1):
                l_found = False
                if x1_s < x1:
                  l_found = True
                if x2_s < x1:
                  l_found = True
                if x1_s < x2:
                  l_found = True
                if x2_s < x2:
                  l_found = True
                if l_found:
                  l += 1
                  continue

            # Check right
            if min(y1_s, y2_s) < max(y1, y2):
                r_found = False
                if x1_s > x1:
                  r_found = True
                if x2_s > x1:
                  r_found = True
                if x1_s > x2:
                  r_found = True
                if x2_s > x2:
                  r_found = True
                if r_found:
                  r += 1
                  continue
            
            if min(y1_s, y2_s) < max(y2, y1):
                r_found = False
                if x1_s > x1:
                  r_found = True
                if x2_s > x1:
                  r_found = True
                if x1_s > x2:
                  r_found = True
                if x2_s > x2:
                  r_found = True
                if r_found:
                  r += 1
                  continue

            # Check top
            if min(x1_s, x2_s) > max(x1, x2):
                t_found = False
                if y1_s < y1:
                  t_found = True
                if y2_s < y1:
                  t_found = True
                if y1_s < y2:
                  t_found = True
                if y2_s < y2:
                  t_found = True
                if t_found:
                  t += 1
                  continue
            
            if min(x1_s, x2_s) > max(x2, x1):
                t_found = False
                if y1_s < y1:
                  t_found = True
                if y2_s < y1:
                  t_found = True
                if y1_s < y2:
                  t_found = True
                if y2_s < y2:
                  t_found = True
                if t_found:
                  t += 1
                  continue

            # Check bottom
            if min(x1_s, x2_s) < max(x1, x2):
                b_found = False
                if y1_s > y1:
                  b_found = True
                if y2_s > y1:
                  b_found = True
                if y1_s > y2:
                  b_found = True
                if y2_s > y2:
                  b_found = True
                if b_found:
                  b += 1
                  continue

            if min(x1_s, x2_s) < max(x2, x1):
                b_found = False
                if y1_s > y1:
                  b_found = True
                if y2_s > y1:
                  b_found = True
                if y1_s > y2:
                  b_found = True
                if y2_s > y2:
                  b_found = True
                if b_found:
                  b += 1
                  continue


        return l, r, t, b

    result = -1
    for i in range(d):
        l, r, t, b = count_sofas(i)
        if l == cnt_l and r == cnt_r and t == cnt_t and b == cnt_b:
            result = i + 1
            break
    
    print(result)

solve()