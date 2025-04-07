def count_bracket_sequences(n, s):
    MOD = 10**9 + 7
    m = len(s)
    
    # Precompute the Catalan numbers up to 2n
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for i in range(1, n + 1):
        catalan[i] = (catalan[i - 1] * (2 * (2 * i - 1)) % MOD * pow(i + 1, MOD - 2, MOD)) % MOD
    
    # Check the validity of the substring s
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)

    # If the balance is not valid or too negative, return 0
    if balance < 0 or balance + n < 0 or min_balance < 0:
        return 0

    # Count the valid configurations around the substring s
    left_needed = (n - (balance + 1)) // 2
    right_needed = (n - (balance - 1)) // 2

    if (n - (balance + 1)) % 2 != 0 or (n - (balance - 1)) % 2 != 0 or left_needed < 0 or right_needed < 0:
        return 0

    # Total valid sequences
    return (catalan[left_needed] * catalan[right_needed]) % MOD

# Input reading
n = int(input().strip())
s = input().strip()

# Calculate and print the result
print(count_bracket_sequences(n, s))