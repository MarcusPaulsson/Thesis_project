def solve():
    n = int(input())
    stats = []
    for _ in range(n):
        stats.append(list(map(int, input().split())))

    possible = True
    for i in range(n):
        if stats[i][1] > stats[i][0]:
            possible = False
            break

        if i > 0:
            if stats[i][0] < stats[i-1][0] or stats[i][1] < stats[i-1][1]:
                possible = False
                break
            if stats[i][0] - stats[i-1][0] < stats[i][1] - stats[i-1][1]:
                possible = False
                break

    if possible:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()