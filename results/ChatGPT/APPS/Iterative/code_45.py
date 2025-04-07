def find_sequence(n, k):
    # Check if it's possible to create such a sequence
    min_sum = k * (k + 1) // 2
    if min_sum > n:
        return -1
    
    # The remaining value after using the first k natural numbers
    remaining = n - min_sum
    
    # The GCD can be maximized by adding the same value to each element
    gcd = remaining // k
    
    # The base sequence is the first k natural numbers
    sequence = [i + gcd for i in range(1, k + 1)]
    
    # Adjust the last element to ensure the sum is exactly n
    sequence[-1] += (remaining % k)
    
    return sequence

# Input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Output
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))