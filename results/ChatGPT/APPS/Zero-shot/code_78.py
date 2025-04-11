def mod_inv(a, p):
    return pow(a, p - 2, p)

def count_regular_sequences(n, s):
    MOD = 10**9 + 7
    m = len(s)
    
    # Precompute factorials and inverse factorials
    fact = [1] * (2 * n + 1)
    for i in range(2, 2 * n + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    inv_fact = [1] * (2 * n + 1)
    inv_fact[2 * n] = mod_inv(fact[2 * n], MOD)
    for i in range(2 * n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    # Check if s can be part of a regular sequence
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
    
    # Count the number of ways to place the remaining brackets
    remaining_open = n - (s.count('('))
    remaining_close = n - (s.count(')'))
    
    # Calculate the number of valid sequences
    total_ways = (fact[remaining_open + remaining_close] * inv_fact[remaining_open] % MOD) * inv_fact[remaining_close] % MOD
    
    return total_ways

n = int(input())
s = input().strip()
print(count_regular_sequences(n, s))