def solve():
    n, L = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for start_diff in range(n):
        shifted_sasha = [(sasha[i] - sasha[0] + kefa[0]) % L for i in range(n)]
        shifted_sasha.sort()

        if shifted_sasha == kefa:
            print("YES")
            return

    print("NO")

solve()