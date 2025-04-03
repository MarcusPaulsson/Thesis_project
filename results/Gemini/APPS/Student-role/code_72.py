def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    unique_elements = sorted(list(set(a)))
    
    if len(unique_elements) > k:
        print(-1)
        return

    
    b = unique_elements + [1] * (k - len(unique_elements))
    
    print(n * k)
    print(*(b * n))

t = int(input())
for _ in range(t):
    solve()