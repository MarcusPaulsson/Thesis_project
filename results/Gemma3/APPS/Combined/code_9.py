def solve():
    d = int(input())
    n, m = map(int, input().split())
    sofas = []
    for _ in range(d):
        x1, y1, x2, y2 = map(int, input().split())
        sofas.append((x1, y1, x2, y2))
    
    cnt_l, cnt_r, cnt_t, cnt_b = map(int, input().split())
    
    def is_left(sofa1, sofa2):
        x1_1, y1_1, x1_2, y1_2 = sofa1
        x2_1, y2_1, x2_2, y2_2 = sofa2
        
        cells1 = [(x1_1, y1_1), (x1_2, y1_2)]
        cells2 = [(x2_1, y2_1), (x2_2, y2_2)]
        
        for a in cells1:
            for b in cells2:
                if a[0] < b[0]:
                    return True
        return False
    
    def is_top(sofa1, sofa2):
        x1_1, y1_1, x1_2, y1_2 = sofa1
        x2_1, y2_1, x2_2, y2_2 = sofa2
        
        cells1 = [(x1_1, y1_1), (x1_2, y1_2)]
        cells2 = [(x2_1, y2_1), (x2_2, y2_2)]
        
        for a in cells1:
            for b in cells2:
                if a[1] < b[1]:
                    return True
        return False
    
    for i in range(d):
        current_sofa = sofas[i]
        
        left_count = 0
        right_count = 0
        top_count = 0
        bottom_count = 0
        
        for j in range(d):
            if i != j:
                other_sofa = sofas[j]
                
                if is_left(other_sofa, current_sofa):
                    left_count += 1
                if is_left(current_sofa, other_sofa):
                    right_count += 1
                if is_top(other_sofa, current_sofa):
                    top_count += 1
                if is_top(current_sofa, other_sofa):
                    bottom_count += 1
        
        if left_count == cnt_l and right_count == cnt_r and top_count == cnt_t and bottom_count == cnt_b:
            print(i + 1)
            return
    
    print(-1)

solve()