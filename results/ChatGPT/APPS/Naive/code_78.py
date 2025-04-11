def count_regular_sequences(n, s):
    MOD = 10**9 + 7
    m = len(s)

    # Precompute Catalan numbers
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for i in range(1, n + 1):
        catalan[i] = (catalan[i - 1] * (2 * (2 * i - 1)) % MOD * pow(i + 1, MOD - 2, MOD)) % MOD

    # Check if s can be part of a valid sequence
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

    # Count valid sequences with s as a substring
    total_count = 0
    for prefix_length in range(max(0, n - (m - 1) - balance), n - balance + 1):
        suffix_length = n - prefix_length - (m - 1)
        if suffix_length < 0:
            continue
        total_count = (total_count + catalan[prefix_length] * catalan[suffix_length]) % MOD

    return total_count

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_regular_sequences(n, s))