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
    for i in range(n):
        if l[i] == 0:
            a[i] = unlocked_values[unlocked_index]
            unlocked_index += 1
    
    print(*a)

t = int(input())
for _ in range(t):
    solve()