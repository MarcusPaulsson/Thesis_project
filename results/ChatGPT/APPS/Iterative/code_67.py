n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)
nice_indices = []

# Count occurrences of each element for quick lookup
from collections import Counter
count = Counter(a)

for i in range(n):
    target = total_sum - a[i]
    if target % 2 == 0:
        target //= 2
        if target in count:
            # Check if we can form the target by removing a[i]
            if (target != a[i] and count[target] > 0) or (target == a[i] and count[target] > 1):
                nice_indices.append(i + 1)

print(len(nice_indices))
if nice_indices:
    print(" ".join(map(str, nice_indices)))