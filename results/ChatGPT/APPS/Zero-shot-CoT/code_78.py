MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)

    # Precompute factorials and inverse factorials
    fact = [1] * (2 * n + 1)
    for i in range(2, 2 * n + 1):
        fact[i] = fact[i - 1] * i % MOD

    inv_fact = [1] * (2 * n + 1)
    inv_fact[2 * n] = pow(fact[2 * n], MOD - 2, MOD)
    for i in range(2 * n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

    # Count the number of open and close brackets in the substring s
    open_count = s.count('(')
    close_count = s.count(')')

    # If s has more closing brackets than opening or too many brackets overall
    if close_count > open_count or open_count > n or close_count > n or open_count + close_count > 2 * n:
        return 0

    # Remaining brackets to fill in the sequence
    remaining_open = n - open_count
    remaining_close = n - close_count

    # Check if we can place the remaining brackets
    if remaining_open < 0 or remaining_close < 0 or remaining_open < remaining_close:
        return 0

    # Calculate the total number of valid regular bracket sequences
    total_sequences = fact[remaining_open + remaining_close] * inv_fact[remaining_open] % MOD * inv_fact[remaining_close] % MOD

    # Now we need to check where we can place the substring s
    # We can place the substring in any position that maintains balance
    balance = 0
    min_balance = 0

    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)

    valid_positions = 0
    for k in range(0, 2 * n - m + 1):
        if k + min_balance >= 0 and remaining_open >= remaining_close:
            valid_positions += 1

    return total_sequences * valid_positions % MOD

# Input reading
n = int(input().strip())
s = input().strip()

# Output result
print(count_regular_sequences(n, s))