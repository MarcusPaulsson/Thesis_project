def find_sequence(n, k):
    # Minimum sum of first k positive integers
    min_sum = k * (k + 1) // 2
    
    if n < min_sum:
        return -1
    
    # The maximum GCD we can use is n // k
    max_gcd = n // k
    
    # We need to find the largest GCD such that the sum of the sequence is n
    for g in range(max_gcd, 0, -1):
        # Calculate the sum of the first k multiples of g
        sum_k_multiples = g * min_sum
        
        if sum_k_multiples <= n and (n - sum_k_multiples) % g == 0:
            # We can form the sequence
            remainder = (n - sum_k_multiples) // g
            sequence = [g * i for i in range(1, k)] + [g * (k + remainder)]
            return sequence
    
    return -1

# Input reading
n, k = map(int, input().split())
result = find_sequence(n, k)

if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))