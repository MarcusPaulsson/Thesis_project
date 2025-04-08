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
        for i in range(d):
            if i != index:
                x1_i, y1_i, x2_i, y2_i = sofas[i]
                x1, y1, x2, y2 = sofas[index]
                
                if min(x1_i, x2_i) < min(x1, x2) and \
                   ((y1_i == y1 and y2_i == y2) or (y1_i == y2 and y2_i == y1)):
                    count += 1
        return count
    
    def count_right(index):
        count = 0
        for i in range(d):
            if i != index:
                x1_i, y1_i, x2_i, y2_i = sofas[i]
                x1, y1, x2, y2 = sofas[index]
                
                if min(x1_i, x2_i) > min(x1, x2) and \
                   ((y1_i == y1 and y2_i == y2) or (y1_i == y2 and y2_i == y1)):
                    count += 1
        return count
    
    def count_top(index):
        count = 0
        for i in range(d):
            if i != index:
                x1_i, y1_i, x2_i, y2_i = sofas[i]
                x1, y1, x2, y2 = sofas[index]
                
                if min(y1_i, y2_i) < min(y1, y2) and \
                   ((x1_i == x1 and x2_i == x2) or (x1_i == x2 and x2_i == x1)):
                    count += 1
        return count
    
    def count_bottom(index):
        count = 0
        for i in range(d):
            if i != index:
                x1_i, y1_i, x2_i, y2_i = sofas[i]
                x1, y1, x2, y2 = sofas[index]
                
                if min(y1_i, y2_i) > min(y1, y2) and \
                   ((x1_i == x1 and x2_i == x2) or (x1_i == x2 and x2_i == x1)):
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