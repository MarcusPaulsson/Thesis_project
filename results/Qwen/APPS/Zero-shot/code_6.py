def min_blow_to_defeat_zmei(n, x, blows):
    blows.sort(key=lambda blow: blow[0] - blow[1])
    blow_count = 0
    for blow in blows:
        if x == 0:
            return blow_count
        heads_cut = min(blow[0], x)
        x -= heads_cut
        x += blow[1]
        blow_count += 1
    return -1 if x > 0 else blow_count

t = int(input())
queries = []
for _ in range(t):
    n, x = map(int, input().split())
    blows = []
    for _ in range(n):
        d, h = map(int, input().split())
        blows.append((d, h))
    queries.append((n, x, blows))

for n, x, blows in queries:
    print(min_blow_to_defeat_zmei(n, x, blows))