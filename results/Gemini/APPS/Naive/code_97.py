def solve():
    n = int(input())
    x = list(map(int, input().split()))

    min_cost = float('inf')

    for target in range(1, 101):
        cost = 0
        for i in range(n):
            cost += abs(x[i] - target) % 2
        min_cost = min(min_cost, cost)

    print(min_cost)

solve()