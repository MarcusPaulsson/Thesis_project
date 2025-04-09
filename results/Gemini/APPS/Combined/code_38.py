def solve():
    n, l = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for shift in range(n):
        shifted_sasha = [(sasha[i] - sasha[0] + l) % l for i in range(n)]
        shifted_sasha.sort()

        kefa_shifted = [(kefa[i] - kefa[0] + l) % l for i in range(n)]
        kefa_shifted.sort()
        

        if shifted_sasha == kefa_shifted:
            print("YES")
            return

    print("NO")

solve()