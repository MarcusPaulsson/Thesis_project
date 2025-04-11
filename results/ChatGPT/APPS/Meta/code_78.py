MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Precompute the number of valid sequences of length 2k
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to form an empty sequence
    
    for k in range(1, n + 1):
        for j in range(k):
            dp[k] = (dp[k] + dp[j] * dp[k - 1 - j]) % MOD
    
    # Check if the given string s can be part of a valid sequence
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)
    
    if balance < 0 or balance > 2 * n or min_balance < 0:
        return 0
    
    # Count the number of valid sequences containing s
    total_count = 0
    
    for prefix_length in range(max(0, -min_balance), n - (balance // 2) + 1):
        suffix_length = n - prefix_length - (m - balance)
        if suffix_length < 0:
            continue
        total_count = (total_count + dp[prefix_length] * dp[suffix_length]) % MOD
    
    return total_count

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_regular_sequences(n, s))