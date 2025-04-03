def solve():
    n, T = map(int, input().split())
    a = list(map(int, input().split()))
    
    colors = [0] * n
    current_color = 0
    
    for i in range(n):
        if a[i] * 2 < T:
            colors[i] = 0
        elif a[i] * 2 > T:
            colors[i] = 1
        else:
            colors[i] = current_color
            current_color = 1 - current_color
            
    print(*colors)

t = int(input())
for _ in range(t):
    solve()