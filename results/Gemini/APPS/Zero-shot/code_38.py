def solve():
    n, L = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for start_diff in range(L):
        possible = True
        kefa_shifted = []
        for dist in kefa:
            kefa_shifted.append((dist + start_diff) % L)
        kefa_shifted.sort()

        if kefa_shifted == sasha:
            print("YES")
            return
    
    print("NO")

solve()