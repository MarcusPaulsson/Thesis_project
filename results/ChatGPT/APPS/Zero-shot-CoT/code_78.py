MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Precompute factorials and inverse factorials
    fact = [1] * (2 * n + 1)
    for i in range(2, 2 * n + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    def mod_inv(x):
        return pow(x, MOD - 2, MOD)
    
    inv_fact = [1] * (2 * n + 1)
    for i in range(2, 2 * n + 1):
        inv_fact[i] = mod_inv(fact[i])
    
    # Check if s can be part of a valid sequence
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
    
    # Count valid sequences
    total_sequences = 0
    for prefix_length in range(max(0, n - (m - balance)), n + 1):
        suffix_length = n - prefix_length
        if suffix_length < 0 or suffix_length + balance < 0:
            continue
        
        # Calculate the number of ways to arrange the remaining brackets
        remaining_open = prefix_length + (balance // 2)
        remaining_close = suffix_length + (balance // 2)
        
        if remaining_open < 0 or remaining_close < 0:
            continue
        
        total_sequences += (fact[remaining_open + remaining_close] * inv_fact[remaining_open] % MOD) * inv_fact[remaining_close] % MOD
        total_sequences %= MOD
    
    return total_sequences

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(count_regular_sequences(n, s))