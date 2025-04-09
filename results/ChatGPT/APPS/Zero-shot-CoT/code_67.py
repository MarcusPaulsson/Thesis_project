n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)
nice_indices = []

for i in range(n):
    if (total_sum - a[i]) == a[i] * 2:  # Check if removing a[i] makes it good
        nice_indices.append(i + 1)  # Store 1-based index

print(len(nice_indices))
if nice_indices:
    print(" ".join(map(str, nice_indices)))