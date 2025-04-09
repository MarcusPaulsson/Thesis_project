n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)
nice_indices = []

for j in range(n):
    remaining_sum = total_sum - a[j]
    if remaining_sum == a[j]:
        nice_indices.append(j + 1)

print(len(nice_indices))
if nice_indices:
    print(" ".join(map(str, nice_indices)))