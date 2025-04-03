def max_beauty(n, x, a):
    # Calculate the original maximum subarray sum (Kadane's algorithm)
    def kadane(arr):
        max_sum = 0
        current_sum = 0
        for value in arr:
            current_sum += value
            if current_sum < 0:
                current_sum = 0
            max_sum = max(max_sum, current_sum)
        return max_sum

    original_beauty = kadane(a)

    # If x is non-positive, multiplying by x won't help, return original beauty
    if x <= 0:
        return original_beauty

    # Calculate the maximum subarray sum considering multiplication by x
    max_with_multiplication = float('-inf')

    # Prefix sums and the max sum we can achieve
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]

    # To find the maximum subarray sum after multiplication by x
    min_prefix = float('inf')
    for i in range(n + 1):
        max_with_multiplication = max(max_with_multiplication, prefix_sum[i] - min_prefix + (prefix_sum[i] - min_prefix) * (x - 1))
        min_prefix = min(min_prefix, prefix_sum[i])

    return max(original_beauty, max_with_multiplication)

# Reading input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Getting the result and printing it
result = max_beauty(n, x, a)
print(result)