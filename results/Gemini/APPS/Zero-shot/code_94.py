def solve():
    n, T = map(int, input().split())
    a = list(map(int, input().split()))
    
    colors = [0] * n
    
    for i in range(n):
        
        if 2 * a[i] < T:
            colors[i] = 0
        elif 2 * a[i] > T:
            colors[i] = 1
        else:
            if i % 2 == 0:
                colors[i] = 0
            else:
                colors[i] = 1
                
    print(*colors)

t = int(input())
for _ in range(t):
    solve()