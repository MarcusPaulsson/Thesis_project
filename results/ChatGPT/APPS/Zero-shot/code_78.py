MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Precompute Catalan numbers up to 2n
    C = [0] * (2 * n + 1)
    C[0] = 1
    for i in range(1, 2 * n + 1):
        C[i] = C[i - 1] * (2 * i - 1) // (i + 1) % MOD

    # Check balance and min balance of s
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)

    if balance < 0 or balance > 2 * n - m or min_balance < 0:
        return 0

    # Count valid placements of s in a valid sequence
    total_count = 0
    for k in range(n + 1):
        if k < -min_balance:  # Not enough opening brackets
            continue
        if k > n + (balance - m) // 2:  # Too many opening brackets
            continue
        
        total_count += C[n - k] * C[n - k + (balance - m) // 2] % MOD
        total_count %= MOD

    return total_count

n = int(input())
s = input().strip()
print(count_regular_sequences(n, s))