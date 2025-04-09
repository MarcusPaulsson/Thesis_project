def solve():
    n = int(input())
    a = list(map(int, input().split()))

    pos_min = a.index(1)
    pos_max = a.index(n)

    ans = 0
    
    # Option 1: Swap 1 to the beginning
    dist1 = abs(0 - pos_max)
    ans = max(ans, dist1)
    
    # Option 2: Swap 1 to the end
    dist2 = abs(n - 1 - pos_max)
    ans = max(ans, dist2)

    # Option 3: Swap n to the beginning
    dist3 = abs(0 - pos_min)
    ans = max(ans, dist3)
    
    # Option 4: Swap n to the end
    dist4 = abs(n - 1 - pos_min)
    ans = max(ans, dist4)

    print(ans)

solve()