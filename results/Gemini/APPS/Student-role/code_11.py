def solve():
    s = input()
    n = len(s)
    
    def calculate_area(commands):
        x, y = 0, 0
        min_x, max_x, min_y, max_y = 0, 0, 0, 0
        
        for cmd in commands:
            if cmd == 'W':
                y -= 1
            elif cmd == 'S':
                y += 1
            elif cmd == 'A':
                x -= 1
            elif cmd == 'D':
                x += 1
            
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
        
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        return width * height
    
    min_area = calculate_area(s)
    
    for i in range(n + 1):
        for cmd in ['W', 'A', 'S', 'D']:
            new_s = s[:i] + cmd + s[i:]
            min_area = min(min_area, calculate_area(new_s))
    
    print(min_area)

t = int(input())
for _ in range(t):
    solve()