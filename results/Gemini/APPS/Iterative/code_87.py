def solve():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))

    pos = []
    neg = []
    for i in range(n):
        if projects[i][1] >= 0:
            pos.append(projects[i])
        else:
            neg.append(projects[i])

    pos.sort(key=lambda x: x[0])
    neg.sort(key=lambda x: x[0] + x[1], reverse=True)

    count = 0
    curr_rating = r
    for a, b in pos:
        if curr_rating >= a:
            curr_rating += b
            count += 1
        else:
            break

    dp = [0] * (2 * 300 * n + 1)
    dp[r] = count

    for a, b in neg:
        for j in range(len(dp) - 1, -1, -1):
            if dp[j] > 0 and j >= a and j + b >= 0:
                dp[j + b] = max(dp[j + b], dp[j] + 1)

    print(max(dp))

solve()