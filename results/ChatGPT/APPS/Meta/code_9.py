d = int(input())
n, m = map(int, input().split())

sofas = []
for i in range(d):
    x1, y1, x2, y2 = map(int, input().split())
    sofas.append((x1, y1, x2, y2))

cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())

def count_relations(sofa):
    x1, y1, x2, y2 = sofa
    count_l = count_r = count_t = count_b = 0
    
    for other in sofas:
        if other == sofa:
            continue
        ox1, oy1, ox2, oy2 = other
        
        # Check left
        if x1 == ox1 and y2 < oy1 and x2 == ox2:
            count_l += 1
        elif x1 == ox1 and oy2 < y1 and x2 == ox2:
            count_r += 1
        
        # Check top
        if y1 == oy1 and x2 < ox1 and y2 == oy2:
            count_t += 1
        elif y1 == oy1 and oy2 < y2 and y2 == oy2:
            count_b += 1
    
    return count_l, count_r, count_t, count_b

for i in range(d):
    counts = count_relations(sofas[i])
    if counts == (cnt_l, cnt_r, cnt_t, cnt_b):
        print(i + 1)
        break
else:
    print(-1)