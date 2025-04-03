def maximum_coins(N):
    coins = 0
    while N > 0:
        if N % 2 == 0:
            take = N // 2
        else:
            take = 1
        coins += take
        N -= take
        if N > 0:
            N -= (N // 2) if N % 2 == 0 else 1
    return coins

T = int(input())
results = []
for _ in range(T):
    N = int(input())
    results.append(maximum_coins(N))

print('\n'.join(map(str, results)))