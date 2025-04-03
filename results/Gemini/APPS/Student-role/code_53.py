def solve():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    
    a.sort()
    
    total_time = 0
    for i in range(n):
        total_time += (a[i] * a[n - 1 - i])
        
    print(total_time % 10007)

solve()