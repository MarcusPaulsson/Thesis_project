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
        
        min_x1 = min(x1_1, x1_2)
        max_x1 = max(x1_1, x1_2)
        min_y1 = min(y1_1, y1_2)
        max_y1 = max(y1_1, y1_2)
        
        min_x2 = min(x2_1, x2_2)
        max_x2 = max(x2_1, x2_2)
        min_y2 = min(y2_1, y2_2)
        max_y2 = max(y2_1, y2_2)

        
        return max_x1 < min_x2
    
    def is_right(sofa1, sofa2):
        x1_1, y1_1, x1_2, y1_2 = sofa1
        x2_1, y2_1, x2_2, y2_2 = sofa2
        
        min_x1 = min(x1_1, x1_2)
        max_x1 = max(x1_1, x1_2)
        min_y1 = min(y1_1, y1_2)
        max_y1 = max(y1_1, y1_2)
        
        min_x2 = min(x2_1, x2_2)
        max_x2 = max(x2_1, x2_2)
        min_y2 = min(y2_1, y2_2)
        max_y2 = max(y2_1, y2_2)

        return max_x2 < min_x1
    
    def is_top(sofa1, sofa2):
        x1_1, y1_1, x1_2, y1_2 = sofa1
        x2_1, y2_1, x2_2, y2_2 = sofa2
        
        min_x1 = min(x1_1, x1_2)
        max_x1 = max(x1_1, x1_2)
        min_y1 = min(y1_1, y1_2)
        max_y1 = max(y1_1, y1_2)
        
        min_x2 = min(x2_1, x2_2)
        max_x2 = max(x2_1, x2_2)
        min_y2 = min(y2_1, y2_2)
        max_y2 = max(y2_1, y2_2)

        return max_y1 < min_y2
    
    def is_bottom(sofa1, sofa2):
        x1_1, y1_1, x1_2, y1_2 = sofa1
        x2_1, y2_1, x2_2, y2_2 = sofa2
        
        min_x1 = min(x1_1, x1_2)
        max_x1 = max(x1_1, x1_2)
        min_y1 = min(y1_1, y1_2)
        max_y1 = max(y1_1, y1_2)
        
        min_x2 = min(x2_1, x2_2)
        max_x2 = max(x2_1, x2_2)
        min_y2 = min(y2_1, y2_2)
        max_y2 = max(y2_1, y2_2)

        return max_y2 < min_y1

    for i in range(d):
        left_count = 0
        right_count = 0
        top_count = 0
        bottom_count = 0
        
        for j in range(d):
            if i != j:
                if is_left(sofas[j], sofas[i]):
                    left_count += 1
                if is_right(sofas[j], sofas[i]):
                    right_count += 1
                if is_top(sofas[j], sofas[i]):
                    top_count += 1
                if is_bottom(sofas[j], sofas[i]):
                    bottom_count += 1
        
        if left_count == cnt_l and right_count == cnt_r and top_count == cnt_t and bottom_count == cnt_b:
            print(i + 1)
            return
    
    print(-1)

solve()