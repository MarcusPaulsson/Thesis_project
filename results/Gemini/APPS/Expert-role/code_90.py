def solve():
    n = int(input())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))

    unlocked_values = []
    for i in range(n):
        if l[i] == 0:
            unlocked_values.append(a[i])

    unlocked_values.sort()

    unlocked_index = 0
    result = []
    for i in range(n):
        if l[i] == 1:
            result.append(a[i])
        else:
            result.append(unlocked_values[unlocked_index])
            unlocked_index += 1

    print(*result)


t = int(input())
for _ in range(t):
    solve()