def max_beauty_with_multiplier(n, x, a):
    def kadane(arr):
        max_ending_here = max_so_far = 0
        for value in arr:
            max_ending_here = max(0, max_ending_here + value)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    max_beauty = kadane(a)

    max_with_multiplier = 0
    current_sum = 0

    # Calculate maximum beauty with multiplier from the start
    for i in range(n):
        current_sum += a[i]
        max_with_multiplier = max(max_with_multiplier, current_sum * x)
        current_sum = max(0, current_sum)

    current_sum = 0
    # Calculate maximum beauty with multiplier from the end
    for i in range(n - 1, -1, -1):
        current_sum += a[i]
        max_with_multiplier = max(max_with_multiplier, current_sum * x)
        current_sum = max(0, current_sum)

    return max(max_beauty, max_with_multiplier)

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(max_beauty_with_multiplier(n, x, a))