MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Precompute the number of valid sequences of length 2k
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to form an empty sequence
    
    for k in range(1, n + 1):
        for j in range(k):
            dp[k] = (dp[k] + dp[j] * dp[k - 1 - j]) % MOD
            
    # Check if s can be a valid substring
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)
    
    if balance < 0 or balance > n or min_balance < 0:
        return 0
    
    # Count valid sequences containing s
    total_count = 0
    
    for prefix_length in range(n + 1):
        suffix_length = n - (m - 1) - prefix_length
        if suffix_length < 0:
            continue
        
        # Count valid prefix sequences of length prefix_length
        prefix_count = dp[prefix_length]
        
        # Count valid suffix sequences of length suffix_length
        suffix_count = dp[suffix_length]
        
        # Valid positions for s in the sequence
        if prefix_length + min_balance >= 0 and prefix_length + balance <= n:
            total_count = (total_count + prefix_count * suffix_count) % MOD
            
    return total_count

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_regular_sequences(n, s))