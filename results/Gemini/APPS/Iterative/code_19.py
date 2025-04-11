def solve():
    n = int(input())
    pairs = []
    for _ in range(n):
        pairs.append(list(map(int, input().split())))

    possible = True
    for i in range(n):
        if pairs[i][1] > pairs[i][0]:
            possible = False
            break
        if i > 0:
            if pairs[i][0] < pairs[i-1][0] or pairs[i][1] < pairs[i-1][1]:
                possible = False
                break
            if pairs[i][0] - pairs[i-1][0] < pairs[i][1] - pairs[i-1][1]:
                possible = False
                break

    if possible:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    solve()