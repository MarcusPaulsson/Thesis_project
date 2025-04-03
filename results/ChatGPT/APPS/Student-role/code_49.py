def count_classy_integers(L, R):
    count = 0
    for i in range(1, R + 1):
        if L <= i <= R:
            if len(str(i).replace('0', '')) <= 3:
                count += 1
    return count

T = int(input())
results = []

for _ in range(T):
    L, R = map(int, input().split())
    results.append(count_classy_integers(L, R))

for result in results:
    print(result)