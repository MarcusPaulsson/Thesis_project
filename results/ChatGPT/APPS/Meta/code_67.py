def find_nice_indices(n, a):
    total_sum = sum(a)
    nice_indices = []

    for i in range(n):
        remaining_sum = total_sum - a[i]
        # Check if the remaining sum is half of total_sum
        if remaining_sum % 2 == 0:
            target = remaining_sum // 2
            # Check if the target exists in the remaining array
            if target in a[:i] + a[i+1:]:
                nice_indices.append(i + 1)  # Store 1-based index

    print(len(nice_indices))
    print(' '.join(map(str, nice_indices)))

# Example usage
n = int(input())
a = list(map(int, input().split()))
find_nice_indices(n, a)