def count_regular_sequences(n, s):
    MOD = 1000000007
    
    # Precompute the Catalan numbers up to 2n
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for i in range(1, n + 1):
        catalan[i] = (catalan[i - 1] * (2 * (2 * i - 1)) % MOD * pow(i + 1, MOD - 2, MOD)) % MOD

    # Check if s is a valid bracket sequence and compute the balance
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)

    # If balance is not zero or min_balance is negative, return 0
    if balance != 0 or min_balance < 0:
        return 0

    total_length = 2 * n
    m = len(s)

    # The number of opening and closing brackets we can still use
    open_brackets_needed = n - (s.count('('))
    close_brackets_needed = n - (s.count(')'))

    # If we can't fill the brackets needed
    if open_brackets_needed < 0 or close_brackets_needed < 0:
        return 0

    # Count valid sequences before and after the substring s
    valid_sequences = 0
    for i in range(open_brackets_needed + 1):
        if i > close_brackets_needed:
            continue
        valid_before = catalan[open_brackets_needed]
        valid_after = catalan[close_brackets_needed]

        valid_sequences = (valid_sequences + valid_before * valid_after) % MOD

    return valid_sequences

# Read input
n = int(input())
s = input().strip()

# Output the result
print(count_regular_sequences(n, s))