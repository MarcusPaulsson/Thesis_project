def find_nice_indices(n, a):
    total_sum = sum(a)
    count = {}
    nice_indices = []

    # Count the occurrences of each element
    for number in a:
        count[number] = count.get(number, 0) + 1

    for i in range(n):
        # Calculate the sum of the remaining elements after removing a[i]
        remaining_sum = total_sum - a[i]

        # Check if remaining_sum is even and calculate the target
        if remaining_sum % 2 == 0:
            target = remaining_sum // 2
            
            # Ensure that the target is in the remaining elements
            # We must ensure that if target is the same as a[i], it occurs more than once
            if (target in count and 
                (target != a[i] or count[target] > 1)):
                nice_indices.append(i + 1)  # Store index as 1-based

    return nice_indices

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Get nice indices
nice_indices = find_nice_indices(n, a)

# Print results
print(len(nice_indices))
if nice_indices:
    print(' '.join(map(str, nice_indices)))