def can_form_palindromic_matrix(n, numbers):
    from collections import Counter
    
    count = Counter(numbers)
    odd_count = 0
    center_element = None
    
    for num, cnt in count.items():
        if cnt % 2 != 0:
            odd_count += 1
            center_element = num
        if odd_count > 1:
            return False, []
    
    matrix = [[0] * n for _ in range(n)]
    half_size = (n * n) // 2
    
    # Fill the matrix
    nums = []
    for num, cnt in count.items():
        nums.extend([num] * (cnt // 2))
    
    if len(nums) < half_size:
        return False, []
    
    idx = 0
    for i in range(n):
        for j in range(n):
            if i < n // 2:
                if j < n // 2:
                    matrix[i][j] = nums[idx]
                    matrix[i][n - j - 1] = nums[idx]
                    matrix[n - i - 1][j] = nums[idx]
                    matrix[n - i - 1][n - j - 1] = nums[idx]
                    idx += 1
                elif n % 2 == 1 and j == n // 2:
                    matrix[i][j] = center_element

    return True, matrix

n = int(input().strip())
numbers = list(map(int, input().strip().split()))

is_possible, result = can_form_palindromic_matrix(n, numbers)

if is_possible:
    print("YES")
    for row in result:
        print(" ".join(map(str, row)))
else:
    print("NO")