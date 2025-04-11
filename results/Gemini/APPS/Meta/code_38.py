def solve():
    n, L = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for shift in range(L):
        shifted_sasha = [(x + shift) % L for x in sasha]
        shifted_sasha.sort()
        if kefa == shifted_sasha:
            print("YES")
            return
    print("NO")

solve()