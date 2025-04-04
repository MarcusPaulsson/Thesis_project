def count_regular_bracket_sequences(n, s):
    MOD = 10**9 + 7
    m = len(s)
    
    # Precompute the dp array for regular bracket sequences
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: 0 pairs
    
    for i in range(n + 1):
        for j in range(n + 1):
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD  # Add a closing bracket
            if i < n:
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD  # Add an opening bracket

    # Helper function to check if a sequence is valid
    def is_valid_sequence(seq):
        balance = 0
        for char in seq:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    # Check the balance of the substring s
    balance_s = 0
    min_balance_s = 0
    for char in s:
        if char == '(':
            balance_s += 1
        else:
            balance_s -= 1
        min_balance_s = min(min_balance_s, balance_s)

    if balance_s < 0 or balance_s > 0 or (n * 2 - m < 0) or (min_balance_s < 0):
        return 0

    result = 0
    for i in range(n - (m - 1) // 2):
        open_needed = (n - (m - 1) // 2) - i
        close_needed = n - open_needed
        if open_needed >= 0 and close_needed >= 0:
            result = (result + dp[open_needed][close_needed]) % MOD

    return result

# Input reading
n = int(input().strip())
s = input().strip()

# Calculate and print result
print(count_regular_bracket_sequences(n, s))