MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Precompute the number of valid sequences of length 2k
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one valid sequence of length 0
    
    for k in range(1, n + 1):
        for j in range(k):
            dp[k] = (dp[k] + dp[j] * dp[k - 1 - j]) % MOD
    
    # Check if s can be a valid substring
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)
    
    if balance < 0 or balance > n or min_balance < 0:
        return 0
    
    # Calculate the number of valid sequences containing s
    total_count = 0
    
    # Try to place s at every possible position
    for i in range(n - (m // 2) + 1):
        left_needed = (m // 2) + i
        right_needed = n - left_needed
        
        if left_needed < 0 or right_needed < 0:
            continue
        
        total_count = (total_count + dp[left_needed] * dp[right_needed]) % MOD
    
    return total_count

n = int(input())
s = input().strip()
print(count_regular_sequences(n, s))