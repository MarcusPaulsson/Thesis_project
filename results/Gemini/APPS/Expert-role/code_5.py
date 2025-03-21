def solve():
    n = int(input())
    a = list(map(int, input().split()))

    results = []
    for l1 in range(1, n):
        l2 = n - l1
        p1 = a[:l1]
        p2 = a[l1:]

        def is_permutation(arr):
            m = len(arr)
            if len(set(arr)) != m:
                return False
            for i in range(1, m + 1):
                if i not in arr:
                    return False
            return True

        if is_permutation(p1) and is_permutation(p2):
            results.append((l1, l2))

    print(len(results))
    for l1, l2 in results:
        print(l1, l2)


t = int(input())
for _ in range(t):
    solve()