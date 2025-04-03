def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    distinct_elements = sorted(list(set(a)))
    if len(distinct_elements) > k:
        print(-1)
        return

    b = distinct_elements + [1] * (k - len(distinct_elements))
    
    print(n * k)
    print(*(b * n))

t = int(input())
for _ in range(t):
    solve()