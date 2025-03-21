def solve():
    s = input()
    n = len(s)
    
    def calculate_grid_area(seq):
        x, y = 0, 0
        min_x, max_x = 0, 0
        min_y, max_y = 0, 0
        
        for move in seq:
            if move == 'W':
                y -= 1
            elif move == 'S':
                y += 1
            elif move == 'A':
                x -= 1
            elif move == 'D':
                x += 1
            
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
        
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        return width * height
    
    best_area = calculate_grid_area(s)
    
    for i in range(n + 1):
        for extra_move in ['W', 'A', 'S', 'D']:
            temp_s = s[:i] + extra_move + s[i:]
            best_area = min(best_area, calculate_grid_area(temp_s))
            
    print(best_area)

t = int(input())
for _ in range(t):
    solve()