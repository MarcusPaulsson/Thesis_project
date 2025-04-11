MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Precompute Catalan numbers up to 2n
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for i in range(1, n + 1):
        catalan[i] = sum(catalan[j] * catalan[i - 1 - j] for j in range(i)) % MOD
    
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
    
    # Count valid sequences with s as a substring
    total_count = 0
    for prefix_length in range(n + 1):
        if prefix_length + m > 2 * n:
            break
        
        prefix_balance = 0
        for i in range(prefix_length):
            prefix_balance += 1  # Assume all '(' in prefix for balance check
        
        if prefix_balance < 0:
            continue
        
        suffix_length = 2 * n - (prefix_length + m)
        suffix_balance = n - (prefix_balance + balance)
        
        if suffix_balance < 0:
            continue
        
        total_count += (catalan[prefix_balance] * catalan[suffix_balance]) % MOD
        total_count %= MOD
    
    return total_count

n = int(input())
s = input().strip()
print(count_regular_sequences(n, s))