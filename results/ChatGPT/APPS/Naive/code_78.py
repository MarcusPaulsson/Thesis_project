MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Precompute the number of valid bracket sequences of length 2*k
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to form an empty sequence

    for k in range(1, n + 1):
        for j in range(k):
            dp[k] = (dp[k] + dp[j] * dp[k - 1 - j]) % MOD

    # Check the balance of the substring s
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)

    # If the balance is not valid or if it goes negative
    if balance < 0 or n < (m + min_balance) // 2:
        return 0

    # Calculate the number of valid sequences containing s
    total_count = 0
    for prefix_length in range(n + 1):
        suffix_length = n - (m - 1) - prefix_length
        if suffix_length < 0:
            continue
        
        # Calculate the required balance for the prefix
        prefix_balance = 0
        for i in range(prefix_length):
            if i < m:
                if s[i] == '(':
                    prefix_balance += 1
                else:
                    prefix_balance -= 1

        # Check if we can form a valid sequence
        if prefix_balance + suffix_length >= 0 and prefix_balance <= n:
            total_count = (total_count + dp[prefix_length] * dp[suffix_length]) % MOD

    return total_count

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_regular_sequences(n, s))