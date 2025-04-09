def max_subarray_sum(arr):
    max_ending_here = 0
    max_so_far = 0
    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_beauty(n, x, a):
    original_beauty = max_subarray_sum(a)
    
    max_increase = 0
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += a[j]
            modified_sum = current_sum * x
            left_sum = max_subarray_sum(a[:i])
            right_sum = max_subarray_sum(a[j + 1:])
            total_sum = left_sum + modified_sum + right_sum
            max_increase = max(max_increase, total_sum)
    
    return max(original_beauty, max_increase)

n, x = map(int, input().split())
a = list(map(int, input().split()))
print(max_beauty(n, x, a))