def max_beauty_with_multiplication(n, x, a):
    # Helper function to calculate maximum subarray sum using Kadane's algorithm
    def kadane(arr):
        max_sum = 0
        current_sum = 0
        for value in arr:
            current_sum += value
            if current_sum < 0:
                current_sum = 0
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    # Calculate the original maximum beauty
    original_beauty = kadane(a)
    
    # Calculate the maximum beauty after multiplying a subarray by x
    max_increase = 0
    current_sum = 0
    
    for i in range(n):
        current_sum += a[i]
        if i == 0:
            max_increase = current_sum * x
        else:
            max_increase = max(max_increase, current_sum * x)
        if current_sum < 0:
            current_sum = 0
    
    # Calculate the maximum beauty after considering the subarray
    max_beauty_after_multiplication = original_beauty + max_increase
    
    return max(max_beauty_after_multiplication, original_beauty)

# Input reading
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output the maximum beauty
print(max_beauty_with_multiplication(n, x, a))