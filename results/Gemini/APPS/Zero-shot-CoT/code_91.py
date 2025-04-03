def solve():
    n = int(input())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))

    unlocked_values = []
    unlocked_indices = []
    for i in range(n):
        if l[i] == 0:
            unlocked_values.append(a[i])
            unlocked_indices.append(i)

    unlocked_values.sort()

    new_a = a[:]
    for i in range(len(unlocked_indices)):
        new_a[unlocked_indices[i]] = unlocked_values[i]

    print(*new_a)


t = int(input())
for _ in range(t):
    solve()