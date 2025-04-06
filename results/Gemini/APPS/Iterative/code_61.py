def solve():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))

    ans = ""
    start = -1
    end = -1

    for i in range(n):
        digit = int(a[i])
        if f[digit - 1] > digit:
            start = i
            break

    if start == -1:
        print(a)
        return

    for i in range(start, n):
        digit = int(a[i])
        if f[digit - 1] >= digit:
            end = i
        else:
            break

    for i in range(n):
        if i < start:
            ans += a[i]
        elif i >= start and i <= end:
            digit = int(a[i])
            ans += str(f[digit - 1])
        else:
            ans += a[i]

    print(ans)

solve()