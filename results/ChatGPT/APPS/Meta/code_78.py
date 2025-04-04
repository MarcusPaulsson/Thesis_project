MOD = 1000000007

def count_regular_bracket_sequences(n, s):
    m = len(s)
    
    # Precompute the number of valid bracket sequences of length 2*k
    # dp[k] means the number of valid sequences of length 2*k
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: there's one valid sequence of length 0 (the empty sequence)

    for k in range(1, n + 1):
        for j in range(k):
            dp[k] = (dp[k] + dp[j] * dp[k - 1 - j]) % MOD

    # Check the required properties of the substring s
    # We will check if the substring s can be a part of a valid sequence of length 2n
    
    # Balance array to check if part of the string is valid
    balance = 0
    min_balance = 0
    
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)

    # If the total balance is not zero or the minimum balance is negative, it's invalid
    if balance < 0 or (n * 2 - m) + balance < 0:
        return 0

    # Remaining open and close brackets we can place
    remaining_open = n - (s.count('('))
    remaining_close = n - (s.count(')'))

    # If we take s as a valid sequence, we need to fill the remaining length
    total_sequences = 0

    for k in range(remaining_open + 1):
        if k <= remaining_close:
            total_sequences = (total_sequences + dp[remaining_open + remaining_close - k]) % MOD

    return total_sequences

# Input reading
n = int(input())
s = input()

# Output the result
print(count_regular_bracket_sequences(n, s))