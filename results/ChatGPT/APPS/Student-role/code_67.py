n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)
nice_indices = []

for i in range(n):
    if (total_sum - a[i]) % 2 == 0:
        target = (total_sum - a[i]) // 2
        if target in a and (target != a[i] or a.count(target) > 1):
            nice_indices.append(i + 1)

print(len(nice_indices))
if nice_indices:
    print(' '.join(map(str, nice_indices)))