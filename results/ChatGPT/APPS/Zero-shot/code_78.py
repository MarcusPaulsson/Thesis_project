MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Precompute Catalan numbers up to 2n
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for i in range(1, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = (catalan[i] + catalan[j] * catalan[i - 1 - j]) % MOD
    
    # Function to check if the current string can be a valid prefix/suffix
    def can_form_prefix(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance
    
    # Check balance of the given string s
    balance = can_form_prefix(s)
    if balance < 0 or balance > n:
        return 0
    
    # Count valid configurations
    valid_count = 0
    for i in range(n + 1):
        if i >= balance and (n - i) >= 0 and (n - i) + balance >= 0:
            valid_count = (valid_count + catalan[i - balance] * catalan[n - i]) % MOD

    return valid_count

# Input reading
n = int(input().strip())
s = input().strip()

# Output result
print(count_regular_sequences(n, s))