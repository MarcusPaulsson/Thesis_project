def solve():
    n, l = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for start_diff in range(l):
        possible = True
        for i in range(n):
            kefa_dist = kefa[i]
            
            found = False
            for j in range(n):
                sasha_dist = sasha[j]
                
                if (kefa_dist - start_diff) % l == sasha_dist:
                    found = True
                    break
            
            if not found:
                possible = False
                break
        
        if possible:
            print("YES")
            return
    
    print("NO")

solve()