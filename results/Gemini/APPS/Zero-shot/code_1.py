def solve():
    n, m, k = map(int, input().split())
    
    if n > k or m > k:
        print(-1)
        return
    
    if n == m:
        print(k)
    else:
        if (k - max(n, m)) % 2 == 0:
            print(k)
        else:
            print(k - 1)

q = int(input())
for _ in range(q):
    solve()