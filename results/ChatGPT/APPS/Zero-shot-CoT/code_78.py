MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Check if s can be a substring of a valid sequence
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
    
    # dp[i][b] = number of valid sequences of length i with balance b
    dp = [[0] * (n + 1) for _ in range(2 * n + 1)]
    dp[0][0] = 1
    
    for i in range(1, 2 * n + 1):
        for b in range(n + 1):
            if b > 0:
                dp[i][b] = dp[i - 1][b - 1]  # Adding '('
            if b < n:
                dp[i][b] += dp[i - 1][b + 1]  # Adding ')'
            dp[i][b] %= MOD
    
    total_count = 0
    
    for start in range(2 * n - m + 1):
        if start > 0:
            prefix_balance = [0] * (start + 1)
            for i in range(start):
                if s[i] == '(':
                    prefix_balance[i + 1] = prefix_balance[i] + 1
                else:
                    prefix_balance[i + 1] = prefix_balance[i] - 1
            if prefix_balance[start] < 0:
                continue
            if prefix_balance[start] + balance < 0:
                continue

        suffix_balance = [0] * (2 * n - (start + m) + 1)
        for i in range(2 * n - (start + m)):
            if s[start + m + i] == '(':
                suffix_balance[i + 1] = suffix_balance[i] + 1
            else:
                suffix_balance[i + 1] = suffix_balance[i] - 1

        if suffix_balance[-1] + balance < 0:
            continue

        # Count valid sequences before s and after s
        prefix_valid = dp[start][0]
        suffix_valid = dp[2 * n - (start + m)][suffix_balance[-1] + balance]
        
        total_count += (prefix_valid * suffix_valid) % MOD
        total_count %= MOD
    
    return total_count

# Read input
n = int(input().strip())
s = input().strip()

# Output the result
print(count_regular_sequences(n, s))