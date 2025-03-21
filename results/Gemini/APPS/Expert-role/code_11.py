def solve():
    s = input()
    n = len(s)
    
    def calculate_grid_size(seq):
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
        
        return (max_x - min_x + 1, max_y - min_y + 1)
    
    best_area = float('inf')
    
    # Original string
    width, height = calculate_grid_size(s)
    best_area = min(best_area, width * height)
    
    # Try inserting each of the four moves at each position
    for i in range(n + 1):
        for move in ['W', 'A', 'S', 'D']:
            new_s = s[:i] + move + s[i:]
            width, height = calculate_grid_size(new_s)
            best_area = min(best_area, width * height)
    
    print(best_area)

t = int(input())
for _ in range(t):
    solve()