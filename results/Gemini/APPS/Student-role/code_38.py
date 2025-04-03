def solve():
    n, k1, k2 = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    max_a = 0
    for x in a:
        max_a = max(max_a, x)
    
    max_b = 0
    for x in b:
        max_b = max(max_b, x)
    
    if max_a > max_b:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()