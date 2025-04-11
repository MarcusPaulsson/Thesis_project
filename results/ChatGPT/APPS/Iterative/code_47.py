def max_subarray_sum(arr):
    max_ending_here = max_so_far = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_beauty_with_multiplier(n, x, a):
    original_beauty = max_subarray_sum(a)

    if x == 0:
        return original_beauty

    max_increase = 0
    current_sum = 0
    for i in range(n):
        current_sum += a[i]
        potential_increase = current_sum * (x - 1)
        max_increase = max(max_increase, potential_increase)
        if current_sum < 0:
            current_sum = 0

    return max(original_beauty, original_beauty + max_increase)

n, x = map(int, input().split())
a = list(map(int, input().split()))

print(max_beauty_with_multiplier(n, x, a))