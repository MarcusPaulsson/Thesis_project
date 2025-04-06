def solve():
    n = int(input())
    a = list(map(int, input().split()))

    for D in range(101):
        for target in range(1, 101):
            possible = True
            for val in a:
                if val == target:
                    continue
                elif val + D == target:
                    continue
                elif val - D == target:
                    continue
                else:
                    possible = False
                    break
            if possible:
                print(D)
                return

    print(-1)

solve()