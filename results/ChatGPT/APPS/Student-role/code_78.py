MOD = 10**9 + 7

def count_regular_bracket_sequences(n, s):
    m = len(s)
    
    # Precompute factorials and inverse factorials for combinations
    fact = [1] * (2 * n + 1)
    for i in range(2, 2 * n + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    def modinv(x):
        return pow(x, MOD - 2, MOD)
    
    if n < m // 2 or n < (m + 1) // 2:  # Not enough pairs to accommodate s
        return 0
    
    # Count the number of '(' and ')' in s
    open_s = s.count('(')
    close_s = s.count(')')
    
    # Check if s can be part of a valid sequence
    if open_s < close_s:
        return 0
    
    # Calculate the number of valid sequences
    total_open = n - open_s
    total_close = n - close_s
    
    if total_open < 0 or total_close < 0:
        return 0
    
    # Count valid sequences that can be formed with remaining brackets
    def count_sequences(open_needed, close_needed):
        if open_needed < 0 or close_needed < 0 or open_needed > close_needed:
            return 0
        return (fact[open_needed + close_needed] * modinv(fact[open_needed]) % MOD) * modinv(fact[close_needed]) % MOD
    
    # Count valid sequences before s
    before_s = count_sequences(n - open_s, n - close_s)
    
    # Count valid sequences after s
    after_s = count_sequences(total_open, total_close)
    
    return before_s * after_s % MOD

# Input
n = int(input().strip())
s = input().strip()

# Output the result
print(count_regular_bracket_sequences(n, s))