def max_prefix_sum(arr1, arr2):
    # Calculate maximum prefix sum for arr1
    max_prefix_sum_a = [0] * (len(arr1) + 1)
    for i in range(1, len(arr1) + 1):
        max_prefix_sum_a[i] = max(max_prefix_sum_a[i - 1] + arr1[i - 1], arr1[i - 1])

    # Calculate maximum prefix sum for arr2
    max_prefix_sum_b = [0] * (len(arr2) + 1)
    for i in range(1, len(arr2) + 1):
        max_prefix_sum_b[i] = max(max_prefix_sum_b[i - 1] + arr2[i - 1], arr2[i - 1])

    # Find the maximum prefix sum by merging both arrays
    max_sum = float('-inf')
    for i in range(len(max_prefix_sum_a)):
        for j in range(len(max_prefix_sum_b)):
            max_sum = max(max_sum, max_prefix_sum_a[i] + max_prefix_sum_b[j])

    return max_sum

# Driver code
if __name__ == "__main__":
    A = [1, -2, 3, 4]
    B = [-1, 2, 3]
    result = max_prefix_sum(A, B)
    print(result)