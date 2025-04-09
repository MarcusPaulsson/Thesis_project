MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Precompute factorials and inverse factorials for combinations
    fact = [1] * (2*n + 1)
    inv_fact = [1] * (2*n + 1)
    
    for i in range(2, 2*n + 1):
        fact[i] = fact[i - 1] * i % MOD

    inv_fact[2*n] = pow(fact[2*n], MOD - 2, MOD)
    for i in range(2*n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    # Function to calculate C(n, k) = n! / (k! * (n-k)!)
    def C(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

    # Check the balance of the string s
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)

    # If the balance is negative or more than n, return 0
    if balance > n or min_balance < 0:
        return 0
    
    # Remaining open and close brackets after placing s
    remaining_open = n - (s.count('('))
    remaining_close = n - (s.count(')'))
    
    result = 0
    for i in range(remaining_open + 1):
        # i is the number of open brackets before s
        # remaining_open - i is the number of open brackets after s
        # remaining_close must match the total number of closing brackets
        result += C(remaining_open, i) * C(remaining_open + remaining_close - 1, remaining_close - 1) % MOD
        result %= MOD

    return result

n = int(input().strip())
s = input().strip()
print(count_regular_sequences(n, s))