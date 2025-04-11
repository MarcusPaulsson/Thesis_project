def count_regular_sequences(n, s):
    MOD = 1000000007
    m = len(s)

    # Precompute the number of valid bracket sequences of length 2k
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to have an empty sequence

    for k in range(1, n + 1):
        for j in range(k):
            dp[k] = (dp[k] + dp[j] * dp[k - 1 - j]) % MOD

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

    # Count the number of valid sequences that can be formed
    total_count = 0
    for prefix in range(n + 1):
        if prefix + balance <= n:
            suffix = n - (prefix + balance)
            if suffix >= 0:
                total_count = (total_count + dp[prefix] * dp[suffix]) % MOD

    return total_count

# Input reading
n = int(input())
s = input().strip()
print(count_regular_sequences(n, s))