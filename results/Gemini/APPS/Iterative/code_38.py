def solve():
    n, l = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for start_diff in range(l):
        possible = True
        kefa_shifted = []
        for i in range(n):
            kefa_shifted.append(kefa[i])
            
        sasha_shifted = []
        for i in range(n):
            sasha_shifted.append((sasha[i] + start_diff) % l)
            
        kefa_shifted.sort()
        sasha_shifted.sort()
            
        if kefa_shifted == sasha_shifted:
            print("YES")
            return

    print("NO")

solve()