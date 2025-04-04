def solve():
    s = input()
    x, y = 0, 0
    visited = set()
    time = 0
    for move in s:
        nx, ny = x, y
        if move == 'N':
            ny += 1
        elif move == 'S':
            ny -= 1
        elif move == 'E':
            nx += 1
        else:
            nx -= 1
        
        segment = tuple(sorted([(x, y), (nx, ny)]))
        
        if segment in visited:
            time += 1
        else:
            time += 5
            visited.add(segment)
        
        x, y = nx, ny
    print(time)

t = int(input())
for _ in range(t):
    solve()