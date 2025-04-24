def solve():
    n, l = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for shift in range(n):
        shifted_sasha = []
        for i in range(n):
            shifted_sasha.append((sasha[i] - sasha[0] + kefa[shift]) % l)
        shifted_sasha.sort()
        kefa_copy = kefa[:]
        kefa_copy.sort()
        if shifted_sasha == kefa_copy:
            print("YES")
            return

    print("NO")

solve()