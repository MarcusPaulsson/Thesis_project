MOD = 10**9 + 7

def count_regular_bracket_sequences(n, s):
    m = len(s)
    
    # Precompute the number of valid sequences of length 2k
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][j] = (dp[i - 1][j + 1] if j + 1 <= i - 1 else 0) + (dp[i - 1][j - 1] if j > 0 else 0)
            dp[i][j] %= MOD

    # Count the number of left and right brackets in s
    left_brackets = s.count('(')
    right_brackets = s.count(')')

    # Validate the brackets count
    if left_brackets < right_brackets or left_brackets > n or right_brackets > n:
        return 0
    
    # Calculate remaining length for valid sequences
    remaining_length = 2 * (n - (left_brackets + right_brackets))

    if remaining_length < 0 or (remaining_length // 2) < 0:
        return 0

    valid_sequences = dp[n - (left_brackets + right_brackets)][0]
    
    # Calculate total sequences by placing `s` in valid sequences
    total_sequences = valid_sequences * (remaining_length + 1) % MOD
    
    return total_sequences

# Read input values
n = int(input().strip())
s = input().strip()

# Compute the result
result = count_regular_bracket_sequences(n, s)
print(result)