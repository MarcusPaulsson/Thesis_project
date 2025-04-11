def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        return

    possible_ds = set()
    for i in range(n):
        for j in range(n):
            diff = abs(a[i] - a[j])
            if diff % 2 == 0:
                possible_ds.add(diff // 2)
    possible_ds.add(0)

    for d in sorted(list(possible_ds)):
        possible_values = set()
        for i in range(n):
            possible_values.add(a[i] + d)
            possible_values.add(a[i] - d)
            possible_values.add(a[i])

        for target in possible_values:
            possible = True
            for i in range(n):
                if a[i] + d == target or a[i] - d == target or a[i] == target:
                    continue
                else:
                    possible = False
                    break
            if possible:
                print(d)
                return

    print(-1)

solve()