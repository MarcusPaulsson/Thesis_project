def find_nice_indices(n, a):
    total_sum = sum(a)
    nice_indices = []

    for i in range(n):
        # Calculate the sum excluding the current element
        remaining_sum = total_sum - a[i]
        # Check if the current element equals the remaining sum
        if remaining_sum % 2 == 0 and (remaining_sum // 2) in (a[:i] + a[i+1:]):
            nice_indices.append(i + 1)  # Store index in 1-based format
    
    return nice_indices

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Find nice indices
nice_indices = find_nice_indices(n, a)

# Output results
print(len(nice_indices))
if nice_indices:
    print(" ".join(map(str, nice_indices)))