def solve():
    q = int(input())
    for _ in range(q):
        n = int(input())
        boards = []
        for _ in range(n):
            a, b = map(int, input().split())
            boards.append((a, b))

        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = boards[0][1]
        dp[0][2] = 2 * boards[0][1]

        for i in range(1, n):
            for j in range(3):
                for k in range(3):
                    if boards[i-1][0] + k != boards[i][0] + j:
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + j * boards[i][1])

        print(min(dp[n-1]))


solve()