MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    min_balance = 0
    current_balance = 0

    for char in s:
        if char == '(':
            current_balance += 1
        else:
            current_balance -= 1
        min_balance = min(min_balance, current_balance)

    if current_balance + n < 0 or current_balance > n:
        return 0

    total_open_needed = (n - current_balance) // 2
    total_close_needed = n - total_open_needed

    if total_open_needed < 0 or total_close_needed < 0:
        return 0

    if min_balance < 0:
        return 0

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(i + 1):
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j] * (j + 1)) % MOD

    return dp[n][0]

def main():
    n = int(input().strip())
    s = input().strip()
    result = count_regular_sequences(n, s)
    print(result)

if __name__ == "__main__":
    main()