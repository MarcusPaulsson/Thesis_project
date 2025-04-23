def solve():
    n, l = map(int, input().split())
    kefa_barriers = list(map(int, input().split()))
    sasha_barriers = list(map(int, input().split()))
    
    for kefa_start in range(l):
        kefa_positions = []
        for barrier in kefa_barriers:
            kefa_positions.append((barrier + kefa_start) % l)
        kefa_positions.sort()
        
        for sasha_start in range(l):
            sasha_positions = []
            for barrier in sasha_barriers:
                sasha_positions.append((barrier + sasha_start) % l)
            sasha_positions.sort()
            
            if kefa_positions == sasha_positions:
                print("YES")
                return
    
    print("NO")

solve()