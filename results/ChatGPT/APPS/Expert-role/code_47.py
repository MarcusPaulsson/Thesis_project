def max_subarray_sum(arr):
    max_ending_here = max_so_far = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_beauty_with_subarray(n, x, a):
    original_beauty = max_subarray_sum(a)

    # Calculate the effect of multiplying a subarray by x
    max_gain = 0
    current_gain = 0

    for i in range(n):
        current_gain += a[i] * x
        # Calculate potential beauty when including the original array sum
        max_gain = max(max_gain, current_gain + original_beauty)

        # Reset current_gain if it drops below 0 (similar to max subarray logic)
        if current_gain < 0:
            current_gain = 0

    return max(max_gain, original_beauty)

n, x = map(int, input().split())
a = list(map(int, input().split()))
print(max_beauty_with_subarray(n, x, a))