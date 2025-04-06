def solve():
    n = int(input())
    s = input()
    ans = n
    for i in range(1, n // 2 + 1):
        if s[:i] == s[i:2 * i]:
            ans = min(ans, i + (n - i))
    print(ans)

solve()