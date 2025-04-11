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

    # Check if s can be part of a regular bracket sequence
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

    # Remaining brackets to place
    remaining_open = n - (s.count('('))
    remaining_close = n - (s.count(')'))

    # Calculate the number of valid sequences
    total_sequences = 0
    for prefix_open in range(remaining_open + 1):
        prefix_close = remaining_open - prefix_open
        if prefix_close < 0 or prefix_close > remaining_close:
            continue

        # Calculate the number of valid sequences with the prefix
        valid_sequences = (fact[remaining_open + remaining_close] * inv_fact[prefix_open] % MOD * inv_fact[prefix_close] % MOD) % MOD
        total_sequences = (total_sequences + valid_sequences) % MOD

    return total_sequences

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(count_regular_sequences(n, s))