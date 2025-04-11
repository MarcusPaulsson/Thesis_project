def find_nice_indices(n, a):
    total_sum = sum(a)
    nice_indices = []

    for i in range(n):
        remaining_sum = total_sum - a[i]
        if remaining_sum % 2 == 0:
            target = remaining_sum // 2
            if target in a[:i] or target in a[i + 1:]:
                nice_indices.append(i + 1)  # Store 1-based index

    return nice_indices

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Finding nice indices
nice_indices = find_nice_indices(n, a)

# Output results
print(len(nice_indices))
if nice_indices:
    print(' '.join(map(str, nice_indices)))