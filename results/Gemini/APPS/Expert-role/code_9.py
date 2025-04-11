def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        sofas.append(list(map(int, input().split())))
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

    def count_left(sofa, sofas_list):
        count = 0
        x1, y1, x2, y2 = sofa
        for other_sofa in sofas_list:
            if sofa == other_sofa:
                continue
            ox1, oy1, ox2, oy2 = other_sofa
            
            if min(y1, y2) > max(oy1, oy2):
                count += 1
            elif max(y1,y2) < min(oy1, oy2):
                continue
            else:
                
                 if min(y1, y2) == min(oy1, oy2) and max(y1, y2) == max(oy1, oy2):
                   if min(x1,x2) < min(ox1,ox2):
                       count +=1
                 else:
                   if min(x1,x2) < min(ox1,ox2) or min(x1,x2) < max(ox1,ox2) :
                       count +=1

        return count

    def count_right(sofa, sofas_list):
        count = 0
        x1, y1, x2, y2 = sofa
        for other_sofa in sofas_list:
            if sofa == other_sofa:
                continue
            ox1, oy1, ox2, oy2 = other_sofa
            
            if min(y1, y2) > max(oy1, oy2):
                continue
            elif max(y1,y2) < min(oy1, oy2):
                count += 1
            else:
                if min(y1, y2) == min(oy1, oy2) and max(y1, y2) == max(oy1, oy2):
                   if max(x1,x2) > max(ox1,ox2):
                       count +=1
                else:
                   if max(x1,x2) > min(ox1,ox2) or max(x1,x2) > max(ox1,ox2) :
                       count +=1

        return count

    def count_top(sofa, sofas_list):
        count = 0
        x1, y1, x2, y2 = sofa
        for other_sofa in sofas_list:
            if sofa == other_sofa:
                continue
            ox1, oy1, ox2, oy2 = other_sofa
            
            if min(x1, x2) > max(ox1, ox2):
                count += 1
            elif max(x1,x2) < min(ox1, ox2):
                continue
            else:
                if min(x1, x2) == min(ox1, ox2) and max(x1, x2) == max(ox1, ox2):
                    if min(y1,y2) < min(oy1,oy2):
                       count +=1
                else:
                    if min(y1,y2) < min(oy1,oy2) or min(y1,y2) < max(oy1,oy2) :
                       count +=1

        return count

    def count_bottom(sofa, sofas_list):
        count = 0
        x1, y1, x2, y2 = sofa
        for other_sofa in sofas_list:
            if sofa == other_sofa:
                continue
            ox1, oy1, ox2, oy2 = other_sofa
            
            if min(x1, x2) > max(ox1, ox2):
                continue
            elif max(x1,x2) < min(ox1, ox2):
                count += 1
            else:
                if min(x1, x2) == min(ox1, ox2) and max(x1, x2) == max(ox1, ox2):
                    if max(y1,y2) > max(oy1,oy2):
                       count +=1
                else:
                    if max(y1,y2) > min(oy1,oy2) or max(y1,y2) > max(oy1,oy2) :
                       count +=1
        return count

    for i in range(d):
        sofa = sofas[i]
        l = count_left(sofa, sofas)
        r = count_right(sofa, sofas)
        t = count_top(sofa, sofas)
        b = count_bottom(sofa, sofas)

        if l == cnt_l and r == cnt_r and t == cnt_t and b == cnt_b:
            print(i + 1)
            return

    print(-1)

solve()