def count_regular_sequences(n, s):
    MOD = 1000000007
    m = len(s)
    
    # Precompute Catalan numbers up to 2n
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for i in range(1, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]
            catalan[i] %= MOD
            
    # Check validity of s
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return 0
            
    if balance + (n - (m - balance)) < 0:
        return 0
    
    # Count valid sequences by placing s in various positions
    result = 0
    for start in range(n - (m // 2) + 1):
        left_needed = (m // 2) + start
        right_needed = n - left_needed
        if left_needed < 0 or right_needed < 0:
            continue
            
        result += (catalan[left_needed] * catalan[right_needed]) % MOD
        result %= MOD
        
    return result

# Read input
n = int(input())
s = input().strip()

# Get the result and print it
result = count_regular_sequences(n, s)
print(result)