def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().split())
        sofas.append((x1, y1, x2, y2))
    
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())
    
    def count_left(index):
        count = 0
        x1, y1, x2, y2 = sofas[index]
        for i in range(d):
            if i != index:
                x1_other, y1_other, x2_other, y2_other = sofas[i]
                
                # Check if sofa i is to the left of sofa index
                if x1_other < x1 or (x1_other == x1 and y1_other < y1):
                    
                    # Check if they overlap
                    if not (x2 < x1_other or x1 > x2_other or y2 < y1_other or y1 > y2_other):
                        count += 1
        return count
    
    def count_right(index):
        count = 0
        x1, y1, x2, y2 = sofas[index]
        for i in range(d):
            if i != index:
                x1_other, y1_other, x2_other, y2_other = sofas[i]
                
                # Check if sofa i is to the right of sofa index
                if x1_other > x2 or (x1_other == x2 and y1_other < y1):
                    
                    # Check if they overlap
                    if not (x2 < x1_other or x1 > x2_other or y2 < y1_other or y1 > y2_other):
                        count += 1
        return count
    
    def count_top(index):
        count = 0
        x1, y1, x2, y2 = sofas[index]
        for i in range(d):
            if i != index:
                x1_other, y1_other, x2_other, y2_other = sofas[i]
                
                # Check if sofa i is to the top of sofa index
                if y1_other < y1 or (y1_other == y1 and x1_other < x1):
                    
                    # Check if they overlap
                    if not (x2 < x1_other or x1 > x2_other or y2 < y1_other or y1 > y2_other):
                        count += 1
        return count
    
    def count_bottom(index):
        count = 0
        x1, y1, x2, y2 = sofas[index]
        for i in range(d):
            if i != index:
                x1_other, y1_other, x2_other, y2_other = sofas[i]
                
                # Check if sofa i is to the bottom of sofa index
                if y1_other > y2 or (y1_other == y2 and x1_other < x1):
                    
                    # Check if they overlap
                    if not (x2 < x1_other or x1 > x2_other or y2 < y1_other or y1 > y2_other):
                        count += 1
        return count

    for i in range(d):
        if (count_left(i) == cnt_l and
            count_right(i) == cnt_r and
            count_top(i) == cnt_t and
            count_bottom(i) == cnt_b):
            print(i + 1)
            return
    
    print(-1)

solve()