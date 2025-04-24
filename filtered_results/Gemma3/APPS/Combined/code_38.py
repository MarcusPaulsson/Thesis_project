def solve():
    n, l = map(int, input().split())
    kefa_barriers = list(map(int, input().split()))
    sasha_barriers = list(map(int, input().split()))

    for kefa_start in range(l):
        kefa_positions = [(barrier - kefa_start) % l for barrier in kefa_barriers]
        kefa_positions.sort()

        for sasha_start in range(l):
            sasha_positions = [(barrier - sasha_start) % l for barrier in sasha_barriers]
            sasha_positions.sort()

            if kefa_positions == sasha_positions:
                print("YES")
                return

    print("NO")

solve()