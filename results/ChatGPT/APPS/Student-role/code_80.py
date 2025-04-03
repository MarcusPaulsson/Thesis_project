def count_pairs(l, r):
    count = 0
    for a in range(l, r + 1):
        for b in range(l, r + 1):
            if a + b == a ^ b:
                count += 1
    return count

t = int(input())
results = []
for _ in range(t):
    l, r = map(int, input().split())
    results.append(count_pairs(l, r))

print('\n'.join(map(str, results)))