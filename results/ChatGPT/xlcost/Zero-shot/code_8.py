def maximize_first_element(arr, K):
    n = len(arr)
    for i in range(1, n):
        if K <= 0:
            break
        cur_val = arr[i]
        while cur_val > 0 and K > 0:
            arr[0] += 1
            cur_val -= 1
            K -= 1
    print(arr[0])

# Driver code
arr = [1, 2, 3, 4]  # Example array
K = 5  # Example K
maximize_first_element(arr, K)