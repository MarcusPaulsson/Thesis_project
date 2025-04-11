def solve():
    n, l = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for shift in range(n):
        shifted_sasha = [(sasha[i] - sasha[0] + l) % l for i in range(n)]
        shifted_sasha.sort()

        diff = kefa[0]
        shifted_kefa = [(kefa[i] - diff + l) % l for i in range(n)]
        shifted_kefa.sort()

        if shifted_kefa == shifted_sasha:
            print("YES")
            return

    print("NO")

solve()