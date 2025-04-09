def find_sequence(n, k):
    # Minimum sum of first k positive integers
    min_sum = k * (k + 1) // 2
    
    if n < min_sum:
        return -1
    
    # Calculate the maximum possible GCD
    max_gcd = n // k
    while max_gcd > 0:
        total = min_sum * max_gcd
        
        if total == n:
            return [i * max_gcd for i in range(1, k + 1)]
        elif total < n:
            remainder = n - total
            if remainder >= k * max_gcd:
                # Distribute the remainder evenly
                base_sequence = [i * max_gcd for i in range(1, k + 1)]
                for i in range(k):
                    base_sequence[i] += remainder // k
                return base_sequence
        
        max_gcd -= 1
    
    return -1

# Input reading
n, k = map(int, input().split())
result = find_sequence(n, k)
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))