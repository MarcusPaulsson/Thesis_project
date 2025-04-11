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

    # Check the balance of the substring s
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)

    if balance < 0 or balance + 2 * n < 0:
        return 0

    # Count valid placements of s in a valid sequence
    total_count = 0
    for prefix_length in range(n + 1):
        suffix_length = n - prefix_length
        if min_balance + prefix_length < 0:
            continue
        
        # Calculate the number of valid sequences
        total_count += (fact[prefix_length + suffix_length] * inv_fact[prefix_length] % MOD * inv_fact[suffix_length] % MOD) % MOD
        total_count %= MOD

    return total_count

n = int(input())
s = input().strip()
print(count_regular_sequences(n, s))