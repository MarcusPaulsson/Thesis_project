def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    total_sum = sum(a)
    
    if total_sum == 0:
        print(0)
        return
    
    a.sort()
    
    transfer_sum = 0
    for i in range(n - 1, n - 1 - k, -1):
        transfer_sum += a[i]
        
    print(transfer_sum)

t = int(input())
for _ in range(t):
    solve()