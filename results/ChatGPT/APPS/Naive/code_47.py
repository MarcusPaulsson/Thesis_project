def max_beauty_with_subarray(n, x, a):
    def kadane(arr):
        max_ending_here = max_so_far = 0
        for num in arr:
            max_ending_here = max(0, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    base_beauty = kadane(a)

    if x == 0:
        return base_beauty

    max_beauty_after_modification = base_beauty

    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += a[end]
            modified_sum = current_sum * x
            new_beauty = kadane(a[:start] + [modified_sum] + a[end+1:])
            max_beauty_after_modification = max(max_beauty_after_modification, new_beauty)

    return max_beauty_after_modification

# Read input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Get the maximum beauty
result = max_beauty_with_subarray(n, x, a)

# Print the result
print(result)