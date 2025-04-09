def find_nice_indices(n, a):
    total_sum = sum(a)
    nice_indices = []

    for i in range(n):
        if (total_sum - a[i]) == a[i]:
            nice_indices.append(i + 1)
        elif (total_sum - a[i]) % 2 == 0:
            target = (total_sum - a[i]) // 2
            if target in a and target != a[i]:
                nice_indices.append(i + 1)

    return nice_indices

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Find nice indices
nice_indices = find_nice_indices(n, a)

# Output result
print(len(nice_indices))
if nice_indices:
    print(' '.join(map(str, nice_indices)))