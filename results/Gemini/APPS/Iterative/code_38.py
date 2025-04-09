def solve():
    n, l = map(int, input().split())
    kefa = list(map(int, input().split()))
    sasha = list(map(int, input().split()))

    for shift in range(l):
        shifted_kefa = sorted([(x + shift) % l for x in kefa])
        if shifted_kefa == sasha:
            print("YES")
            return

    print("NO")

solve()