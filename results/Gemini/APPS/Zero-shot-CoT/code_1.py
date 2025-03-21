def solve():
    q = int(input())
    for _ in range(q):
        n, m, k = map(int, input().split())
        
        if n > k or m > k:
            print(-1)
            continue
        
        if n == m:
            print(k)
        else:
            if (k - max(n, m)) % 2 == 0:
                print(k)
            else:
                print(k - 2)

solve()