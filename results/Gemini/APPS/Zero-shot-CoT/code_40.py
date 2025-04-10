def solve():
    n, l = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))
    
    for shift in range(l):
        shifted_sasha = [(x + shift) % l for x in sasha]
        shifted_sasha.sort()
        
        if kefa == shifted_sasha:
            print("YES")
            return
    
    print("NO")

solve()