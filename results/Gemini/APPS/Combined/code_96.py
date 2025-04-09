def solve():
    n = int(input())
    q = list(map(int, input().split()))

    for first_element in range(1, n + 1):
        p = [first_element]
        for i in range(n - 1):
            p.append(p[-1] + q[i])

        if len(set(p)) != n or any(x < 1 or x > n for x in p):
            continue
        
        permutation = sorted(p)
        is_permutation = True
        for i in range(n):
            if permutation[i] != i + 1:
                is_permutation = False
                break
        if is_permutation:
            print(*p)
            return

    print(-1)

solve()