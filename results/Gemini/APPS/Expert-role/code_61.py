def solve():
    n = int(input())
    p = list(map(int, input().split()))

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if p[i] < p[j] and p[j] > p[k]:
                    print("YES")
                    print(i + 1, j + 1, k + 1)
                    return

    print("NO")


t = int(input())
for _ in range(t):
    solve()