MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Check if s can be a valid substring in regular bracket sequences
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)

    if balance < 0 or min_balance < 0:
        return 0

    # dp[i][j] means the number of valid sequences of length i with balance j
    dp = [[0] * (n + 1) for _ in range(2 * n + 1)]
    dp[0][0] = 1

    for i in range(1, 2 * n + 1):
        for j in range(n + 1):
            # Add '('
            if j + 1 <= n:
                dp[i][j + 1] = (dp[i][j + 1] + dp[i - 1][j]) % MOD
            # Add ')'
            if j - 1 >= 0:
                dp[i][j - 1] = (dp[i][j - 1] + dp[i - 1][j]) % MOD

    total_sequences = 0
    
    # Now we need to count valid sequences that contain s as a substring
    for start in range(2 * n - m + 1):
        valid = True
        temp_balance = 0
        for i in range(m):
            if s[i] == '(':
                temp_balance += 1
            else:
                temp_balance -= 1
            if temp_balance < 0:
                valid = False
                break
        
        if valid:
            # Check remaining positions
            remaining_length = 2 * n - (start + m)
            left_balance = balance
            right_balance = n - left_balance
            
            if remaining_length % 2 == 0 and left_balance <= n and right_balance <= n:
                total_sequences = (total_sequences + dp[remaining_length][left_balance]) % MOD

    return total_sequences

n = int(input())
s = input().strip()
print(count_regular_sequences(n, s))