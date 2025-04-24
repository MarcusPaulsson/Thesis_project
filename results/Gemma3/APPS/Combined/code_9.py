def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().split())
        sofas.append((x1, y1, x2, y2))
    
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())
    
    for i in range(d):
        x1, y1, x2, y2 = sofas[i]
        
        left_count = 0
        right_count = 0
        top_count = 0
        bottom_count = 0
        
        for j in range(d):
            if i == j:
                continue
            
            x1_other, y1_other, x2_other, y2_other = sofas[j]
            
            # Check left
            if x1_other < x1:
                if not (x2_other < x1 or x1 > x2_other or y1_other > y2 or y2 < y1_other):
                    left_count += 1
            
            # Check right
            if x1_other > x1:
                if not (x2_other < x1 or x1 > x2_other or y1_other > y2 or y2 < y1_other):
                    right_count += 1
            
            # Check top
            if y1_other < y1:
                if not (x2_other < x1 or x1 > x2_other or y1_other > y2 or y2 < y1_other):
                    top_count += 1
            
            # Check bottom
            if y1_other > y1:
                if not (x2_other < x1 or x1 > x2_other or y1_other > y2 or y2 < y1_other):
                    bottom_count += 1
        
        if left_count == cnt_l and right_count == cnt_r and top_count == cnt_t and bottom_count == cnt_b:
            print(i + 1)
            return
    
    print(-1)

solve()