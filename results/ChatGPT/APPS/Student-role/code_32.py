def maximum_coins(N):
    return N // 2

T = int(input())
results = []
for _ in range(T):
    N = int(input())
    results.append(maximum_coins(N))

print('\n'.join(map(str, results)))