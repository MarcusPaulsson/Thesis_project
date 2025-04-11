def count_regular_sequences(n, s):
    MOD = 10**9 + 7
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
        balance += 1 if char == '(' else -1
        min_balance = min(min_balance, balance)

    if balance < 0 or balance > 2 * n or min_balance < 0:
        return 0

    # Count valid sequences
    total_sequences = 0
    for prefix_length in range(n + 1):
        suffix_length = n - prefix_length
        if prefix_length + m + suffix_length == n:
            total_sequences += (fact[prefix_length + suffix_length] * inv_fact[prefix_length] % MOD * inv_fact[suffix_length] % MOD)
            total_sequences %= MOD

    return total_sequences

# Read input
n = int(input())
s = input().strip()

# Output the result
print(count_regular_sequences(n, s))