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
    
    # Count the number of valid sequences of length 2n
    total_valid_sequences = 0
    
    for prefix_length in range(n + 1):
        suffix_length = n - prefix_length
        if suffix_length < 0:
            continue
        
        # Valid prefix must have a balance of 0 at the end
        prefix_balance = prefix_length - (n - prefix_length)
        
        if prefix_balance < 0:
            continue
        
        # Valid suffix must also have a balance of 0 at the end
        suffix_balance = suffix_length - (n - suffix_length)
        
        if suffix_balance < 0:
            continue
        
        # Count valid sequences
        total_valid_sequences += (fact[prefix_length] * inv_fact[prefix_length // 2] % MOD) * (fact[suffix_length] * inv_fact[suffix_length // 2] % MOD) % MOD
        total_valid_sequences %= MOD
    
    return total_valid_sequences

n = int(input())
s = input().strip()
print(count_regular_sequences(n, s))