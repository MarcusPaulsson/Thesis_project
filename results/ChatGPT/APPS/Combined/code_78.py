MOD = 1000000007

def count_regular_sequences(n, s):
    len_s = len(s)
    current_balance = 0
    min_balance = 0

    # Calculate current balance and minimum balance for the substring s
    for char in s:
        if char == '(':
            current_balance += 1
        else:
            current_balance -= 1
        min_balance = min(min_balance, current_balance)

    # Validity check for substring s
    if current_balance < 0 or current_balance + n < len_s or min_balance < 0:
        return 0

    # Dynamic programming table to count valid bracket sequences
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: one way to have an empty sequence

    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][j] = dp[i - 1][j]  # Add a closing bracket
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]  # Add an opening bracket
            dp[i][j] %= MOD

    # Calculate valid sequences that can be formed with remaining brackets
    valid_sequences = 0
    for k in range(n + 1):
        if 0 <= k + current_balance <= n:
            valid_sequences += dp[n - len_s][k + current_balance]
            valid_sequences %= MOD

    return valid_sequences

# Read input
n = int(input().strip())
s = input().strip()

# Output result
print(count_regular_sequences(n, s))