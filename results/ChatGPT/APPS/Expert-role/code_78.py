def count_regular_sequences(n, s):
    MOD = 1000000007
    m = len(s)
    
    # Precompute the number of valid bracket sequences of length 2k
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one valid sequence of length 0 (the empty sequence)
    
    for k in range(1, n + 1):
        for j in range(k):
            dp[k] = (dp[k] + dp[j] * dp[k - 1 - j]) % MOD
    
    # Check if the string s can be a substring of a valid sequence of length 2n
    bal = 0
    min_bal = 0
    for char in s:
        if char == '(':
            bal += 1
        else:
            bal -= 1
        min_bal = min(min_bal, bal)
    
    # If the balance is negative or the final balance is not zero, return 0
    if bal < 0 or bal > n or (n - bal) < 0 or (n - bal) % 2 != 0:
        return 0
    
    # Calculate the necessary opening and closing brackets
    open_needed = (n - bal) // 2
    close_needed = n - open_needed
    
    if open_needed < 0 or close_needed < 0 or open_needed + close_needed != n:
        return 0
    
    # Count valid sequences
    total_sequences = dp[n]
    
    # Now, we need to calculate the valid sequences that can be formed around s
    count = 0
    for i in range(max(0, open_needed - min_bal), min(open_needed, n - m + 1) + 1):
        left_open = open_needed - i
        right_open = n - (m + left_open)
        if right_open < 0:
            continue
        count = (count + dp[left_open] * dp[right_open]) % MOD
    
    return count

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_regular_sequences(n, s))