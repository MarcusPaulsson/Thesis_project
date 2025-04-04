def count_regular_sequences(n, s):
    MOD = 1000000007
    m = len(s)

    # Check if s can be part of a regular bracket sequence
    balance = 0
    min_balance = 0
    for char in s:
        balance += 1 if char == '(' else -1
        min_balance = min(min_balance, balance)

    # If the balance is not zero or min_balance < 0, it can't be part of a valid sequence
    if balance != 0 or min_balance < 0:
        return 0

    # Calculate the number of valid sequences of length 2n
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n + 1):
            if j < n:
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD  # Adding '('
            if j > 0:
                dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD  # Adding ')'

    total_sequences = dp[n][0]

    # Count the number of ways to place s in the regular sequences
    count = 0
    for i in range(n - m + 1):
        left_balance = sum(1 if s[j] == '(' else -1 for j in range(i))
        right_balance = sum(1 if s[j] == '(' else -1 for j in range(i + m, n))

        if left_balance < 0 or right_balance < 0:
            continue

        ways_left = dp[i][left_balance]
        ways_right = dp[n - (i + m)][right_balance]
        count = (count + ways_left * ways_right) % MOD

    return count


# Read input
n = int(input().strip())
s = input().strip()

# Output the result
print(count_regular_sequences(n, s))