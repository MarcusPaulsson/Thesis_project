def solve():
    n = int(input())
    x = list(map(int, input().split()))

    min_cost = float('inf')

    for target in set(x):
        cost = 0
        for val in x:
            cost += abs(val - target) % 2
        min_cost = min(min_cost, cost)

    print(min_cost)

solve()