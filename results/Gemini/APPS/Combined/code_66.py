def solve():
    n, k = map(int, input().split())
    t = input()

    if k == 1:
        print(t)
        return

    overlap = 0
    for i in range(1, n):
        if t[:n - i] == t[i:]:
            overlap = n - i
            break

    result = t
    for _ in range(k - 1):
        result += t[overlap:]

    print(result)

solve()