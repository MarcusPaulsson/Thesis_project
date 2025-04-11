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
    for i in range(2 * n + 1):
        inv_fact[i] = mod_inv(fact[i])
    
    # Check if s can be part of a regular bracket sequence
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)
    
    if balance < 0 or n < (m + min_balance) // 2:
        return 0
    
    # Count the number of valid sequences
    total_open = (n - (m + min_balance) // 2)
    total_close = (n - (m - min_balance) // 2)
    
    if total_open < 0 or total_close < 0:
        return 0
    
    result = (fact[total_open + total_close] * inv_fact[total_open] % MOD) * inv_fact[total_close] % MOD
    return result

n = int(input())
s = input().strip()
print(count_regular_sequences(n, s))