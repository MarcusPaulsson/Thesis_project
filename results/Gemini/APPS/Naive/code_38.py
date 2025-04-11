def solve():
    n, l = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for start_diff in range(l):
        possible = True
        for i in range(n):
            kefa_dist = kefa[i]
            sasha_dist = (sasha[0] + start_diff) % l
            
            found = False
            for j in range(n):
                if (sasha[j] + start_diff) % l == kefa_dist:
                    found = True
                    break
            if not found:
                possible = False
                break
        
        if possible:
            
            kefa_shifted = []
            for i in range(n):
                kefa_shifted.append(kefa[i])
            
            sasha_shifted = []
            for i in range(n):
                sasha_shifted.append((sasha[i] + start_diff) % l)
            
            sasha_shifted.sort()
            kefa_shifted.sort()
            
            if sasha_shifted == kefa_shifted:
                print("YES")
                return
    
    print("NO")

solve()