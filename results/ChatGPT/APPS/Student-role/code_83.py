t = int(input())
for _ in range(t):
    x, y, a, b = map(int, input().split())
    distance = y - x
    total_hops = a + b
    
    if distance % total_hops == 0:
        print(distance // total_hops)
    else:
        print(-1)