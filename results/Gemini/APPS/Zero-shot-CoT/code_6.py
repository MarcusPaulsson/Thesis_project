def solve():
    n, x = map(int, input().split())
    blows = []
    for _ in range(n):
        blows.append(list(map(int, input().split())))

    ans = float('inf')

    for i in range(n):
        if blows[i][0] >= x:
            ans = min(ans, 1)
            
    if ans == 1:
        print(1)
        return
        
    
    max_diff = 0
    max_damage = 0
    
    for d, h in blows:
        max_diff = max(max_diff, d - h)
        max_damage = max(max_damage, d)
        
    if max_diff <= 0:
        if max_damage >= x:
            print(1)
        else:
            print(-1)
        return

    
    remaining = x - max_damage
    
    if remaining <= 0:
        print(1)
        return
    
    
    num_blows = (remaining + max_diff - 1) // max_diff
    
    print(num_blows + 1)


t = int(input())
for _ in range(t):
    solve()