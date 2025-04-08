def max_beauty_with_multiplication(n, x, a):
    def kadane(arr):
        max_sum = 0
        current_sum = 0
        for value in arr:
            current_sum += value
            max_sum = max(max_sum, current_sum)
            current_sum = max(current_sum, 0)
        return max_sum

    # Calculate the maximum beauty without any multiplication
    max_beauty = kadane(a)

    # Prepare to find the maximum beauty with multiplication
    total_sum = sum(a)
    max_subarray_sum_with_multiplier = float('-inf')

    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += a[end]
            # Calculate potential new beauty with this subarray multiplied by x
            modified_sum = current_sum * x
            new_beauty = total_sum - current_sum + modified_sum
            max_subarray_sum_with_multiplier = max(max_subarray_sum_with_multiplier, new_beauty)

    # The result is the maximum of the beauty without multiplication and with multiplication
    return max(max_beauty, max_subarray_sum_with_multiplier)

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(max_beauty_with_multiplication(n, x, a))