def find_nice_indices(n, a):
    total_sum = sum(a)
    nice_indices = []
    count = {}

    # Count occurrences of each element
    for num in a:
        count[num] = count.get(num, 0) + 1

    for i in range(n):
        current_value = a[i]
        remaining_sum = total_sum - current_value
        
        # Check if the remaining sum is even and if the target can be found
        if remaining_sum % 2 == 0:
            target = remaining_sum // 2
            if target in count:
                # Ensure we have enough occurrences of target
                if (target != current_value and count[target] > 0) or (target == current_value and count[target] > 1):
                    nice_indices.append(i + 1)  # Store 1-based index

    return nice_indices

# Read input
n = int(input())
a = list(map(int, input().split()))

# Find nice indices
nice_indices = find_nice_indices(n, a)

# Print output
print(len(nice_indices))
if nice_indices:
    print(" ".join(map(str, nice_indices)))