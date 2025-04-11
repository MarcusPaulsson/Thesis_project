MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Precompute Catalan numbers
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for i in range(1, n + 1):
        catalan[i] = (catalan[i - 1] * (2 * (2 * i - 1)) % MOD * pow(i + 1, MOD - 2, MOD)) % MOD
    
    # Check the balance of the substring s
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)
    
    if balance < 0 or balance > 2 * n - m:
        return 0
    
    # Calculate the number of valid sequences
    total_count = 0
    for prefix in range(n + 1):
        if prefix + balance < 0 or prefix + balance > n:
            continue
        suffix = n - prefix - (balance + (n - m) // 2)
        if suffix < 0 or suffix > n:
            continue
        total_count = (total_count + catalan[prefix] * catalan[suffix]) % MOD
    
    return total_count

n = int(input())
s = input().strip()
print(count_regular_sequences(n, s))