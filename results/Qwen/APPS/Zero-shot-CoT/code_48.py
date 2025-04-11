import sys
import math

def kth_largest_in_multiplication_table(n, m, k):
    if n > m:
        n, m = m, n
    
    def count_numbers_less_than_or_equal(x):
        count = 0
        for i in range(1, n + 1):
            count += min(x // i, m)
        return count
    
    left, right = 1, n * m
    while left < right:
        mid = (left + right) // 2
        if count_numbers_less_than_or_equal(mid) < k:
            left = mid + 1
        else:
            right = mid
    
    return left

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    print(kth_largest_in_multiplication_table(n, m, k))