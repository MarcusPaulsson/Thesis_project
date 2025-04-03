def find_nice_indices(n, a):
    total_sum = sum(a)
    nice_indices = []

    for i in range(n):
        remaining_sum = total_sum - a[i]
        if remaining_sum == a[i] * 2:
            nice_indices.append(i + 1)

    return nice_indices

# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Find nice indices
nice_indices = find_nice_indices(n, a)

# Output the results
print(len(nice_indices))
if nice_indices:
    print(' '.join(map(str, nice_indices)))