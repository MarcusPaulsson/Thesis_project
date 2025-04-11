def find_nice_indices(n, a):
    total_sum = sum(a)
    nice_indices = []
    element_count = {}

    # Count occurrences of each element
    for num in a:
        element_count[num] = element_count.get(num, 0) + 1

    for i in range(n):
        remaining_sum = total_sum - a[i]

        # Check if remaining_sum is even and if half of it exists in the array
        if remaining_sum % 2 == 0:
            target = remaining_sum // 2
            # Check if target exists in the element count
            if target in element_count:
                # Ensure we are not counting the removed element itself
                if target != a[i] or element_count[target] > 1:
                    nice_indices.append(i + 1)  # Store 1-based index

    return nice_indices

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Find nice indices
nice_indices = find_nice_indices(n, a)

# Output results
print(len(nice_indices))
if nice_indices:
    print(' '.join(map(str, nice_indices)))