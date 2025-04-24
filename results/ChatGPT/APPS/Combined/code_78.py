MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    
    # Precompute the Catalan numbers up to 2n
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for i in range(1, n + 1):
        catalan[i] = sum(catalan[j] * catalan[i - 1 - j] for j in range(i)) % MOD

    # Check the balance of the substring s
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)

    # If the total balance is negative or cannot be balanced with n pairs
    if balance < 0 or balance + n < 0:
        return 0

    # Count the number of valid sequences
    total_count = 0
    for prefix_length in range(n + 1):
        if prefix_length + m > 2 * n:
            break
        
        prefix_balance = prefix_length + min_balance
        suffix_balance = n - (prefix_length + balance)
        
        if prefix_balance < 0 or suffix_balance < 0:
            continue
        
        total_count += (catalan[prefix_balance] * catalan[suffix_balance]) % MOD
        total_count %= MOD

    return total_count

# Input reading
n = int(input().strip())
s = input().strip()

# Output the result
print(count_regular_sequences(n, s))