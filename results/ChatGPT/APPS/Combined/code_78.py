MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Precompute the number of valid sequences of length 2k
    dp = [[0] * (n + 1) for _ in range(2 * n + 1)]
    dp[0][0] = 1
    
    for i in range(1, 2 * n + 1):
        for j in range(n + 1):
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD
            if j < n:
                dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % MOD

    # Calculate the balance of the string s
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)

    # Check if the balance is valid
    if balance < 0 or balance > n or (n - balance) < -min_balance:
        return 0

    # Count valid sequences with s as a substring
    total_count = 0
    for i in range(n - (balance - min_balance) + 1):
        total_count = (total_count + dp[2 * (n - i)][(n - i) + min_balance]) % MOD

    return total_count

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_regular_sequences(n, s))