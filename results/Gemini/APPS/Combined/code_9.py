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
        x_coords = [min(sofas[sofa_index][0][0], sofas[sofa_index][1][0])]
        y_coords = [sofas[sofa_index][0][1], sofas[sofa_index][1][1]]
        
        for i in range(d):
            if i != sofa_index:
                other_x_max = max(sofas[i][0][0], sofas[i][1][0])
                other_y_min = min(sofas[i][0][1], sofas[i][1][1])
                other_y_max = max(sofas[i][0][1], sofas[i][1][1])
                
                if min(y_coords) <= other_y_max and max(y_coords) >= other_y_min:
                    if min(x_coords) > other_x_max:
                        count += 1
        return count

    def count_right(sofa_index):
        count = 0
        x_coords = [max(sofas[sofa_index][0][0], sofas[sofa_index][1][0])]
        y_coords = [sofas[sofa_index][0][1], sofas[sofa_index][1][1]]
        
        for i in range(d):
            if i != sofa_index:
                other_x_min = min(sofas[i][0][0], sofas[i][1][0])
                other_y_min = min(sofas[i][0][1], sofas[i][1][1])
                other_y_max = max(sofas[i][0][1], sofas[i][1][1])
                
                if min(y_coords) <= other_y_max and max(y_coords) >= other_y_min:
                    if max(x_coords) < other_x_min:
                        count += 1
        return count

    def count_top(sofa_index):
        count = 0
        y_coords = [min(sofas[sofa_index][0][1], sofas[sofa_index][1][1])]
        x_coords = [sofas[sofa_index][0][0], sofas[sofa_index][1][0]]
        
        for i in range(d):
            if i != sofa_index:
                other_y_max = max(sofas[i][0][1], sofas[i][1][1])
                other_x_min = min(sofas[i][0][0], sofas[i][1][0])
                other_x_max = max(sofas[i][0][0], sofas[i][1][0])
                
                if min(x_coords) <= other_x_max and max(x_coords) >= other_x_min:
                    if min(y_coords) > other_y_max:
                        count += 1
        return count

    def count_bottom(sofa_index):
        count = 0
        y_coords = [max(sofas[sofa_index][0][1], sofas[sofa_index][1][1])]
        x_coords = [sofas[sofa_index][0][0], sofas[sofa_index][1][0]]
        
        for i in range(d):
            if i != sofa_index:
                other_y_min = min(sofas[i][0][1], sofas[i][1][1])
                other_x_min = min(sofas[i][0][0], sofas[i][1][0])
                other_x_max = max(sofas[i][0][0], sofas[i][1][0])
                
                if min(x_coords) <= other_x_max and max(x_coords) >= other_x_min:
                    if max(y_coords) < other_y_min:
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