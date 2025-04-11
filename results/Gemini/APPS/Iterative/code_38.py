def solve():
    n, L = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for start_diff in range(L):
        possible = True
        for i in range(n):
            if (sasha[i] + start_diff) % L not in kefa:
                possible = False
                break
        
        if possible:
            kefa_pos = []
            for i in range(n):
                kefa_pos.append(kefa[i])
            
            sasha_pos = []
            for i in range(n):
                sasha_pos.append((sasha[i] + start_diff) % L)
            
            kefa_pos.sort()
            sasha_pos.sort()
            
            if kefa_pos == sasha_pos:
                print("YES")
                return
    
    print("NO")

solve()