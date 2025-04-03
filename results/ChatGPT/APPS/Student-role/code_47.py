def max_beauty_after_multiplication(n, x, a):
    def kadane(arr):
        max_ending_here = 0
        max_so_far = 0
        for num in arr:
            max_ending_here = max(0, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Original beauty of the array
    original_beauty = kadane(a)
    
    # Calculate the maximum beauty after multiplying a subarray by x
    max_beauty_with_multiplication = original_beauty
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += a[end]
            modified_sum = current_sum * x
            new_beauty = kadane(a[:start] + [modified_sum] + a[end+1:])
            max_beauty_with_multiplication = max(max_beauty_with_multiplication, new_beauty)

    return max_beauty_with_multiplication

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(max_beauty_after_multiplication(n, x, a))