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
                if (sasha[j] + start_diff) % l == kefa[i]:
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