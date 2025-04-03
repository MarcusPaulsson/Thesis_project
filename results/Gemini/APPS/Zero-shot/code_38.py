def solve():
    n, l = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for shift in range(l):
        shifted_sasha = []
        for dist in sasha:
            shifted_dist = (dist + shift) % l
            shifted_sasha.append(shifted_dist)
        
        shifted_sasha.sort()
        
        if shifted_sasha == kefa:
            print("YES")
            return
    
    print("NO")

solve()