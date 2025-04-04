n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)
nice_indices = []

for i in range(n):
    if a[i] == total_sum - a[i]:
        nice_indices.append(i + 1)

print(len(nice_indices))
if nice_indices:
    print(*nice_indices)