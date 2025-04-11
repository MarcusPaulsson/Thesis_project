def max_beauty_with_subarray(n, x, a):
    def kadane(arr):
        max_ending_here = max_so_far = 0
        for value in arr:
            max_ending_here = max(0, max_ending_here + value)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    original_beauty = kadane(a)

    max_increase = 0
    current_sum = 0
    for value in a:
        current_sum += value
        max_increase = max(max_increase, current_sum * x)
        if current_sum < 0:
            current_sum = 0

    max_beauty = max(original_beauty, original_beauty + max_increase)

    return max_beauty