MOD = 10**9 + 7

def count_regular_sequences(n, s):
    len_s = len(s)
    
    # Precompute the number of ways to form regular bracket sequences of length 2k
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for k in range(1, n + 1):
        for j in range(k):
            dp[k] = (dp[k] + dp[j] * dp[k - 1 - j]) % MOD
            
    total_regular_sequences = dp[n]
    
    # Check how many open and close brackets are in s
    open_s = s.count('(')
    close_s = s.count(')')
    
    # If s has more close brackets than open brackets, it's impossible
    if open_s < close_s or open_s > n or close_s > n:
        return 0
    
    # We need to find valid placements for s in the regular sequence
    valid_count = 0
    
    for start in range(n - (len_s - 1) + 1):
        open_before = start
        close_before = (n - 1) - (len_s - 1 - open_s) - start
        
        # Check if it is valid to insert s here
        if open_before < close_before:
            continue
        
        # Total remaining open and close brackets
        remaining_open = n - open_s
        remaining_close = n - close_s
        
        # Valid placements count
        if remaining_open >= remaining_close:
            valid_count += dp[remaining_open]
            valid_count %= MOD
            
    return valid_count

# Input reading
n = int(input())
s = input().strip()

# Calculate the result
result = count_regular_sequences(n, s)

# Output the result
print(result)