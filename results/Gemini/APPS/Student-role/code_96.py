def solve():
    n = int(input())
    q = list(map(int, input().split()))

    for first_element in range(1, n + 1):
        p = [first_element]
        valid = True
        for i in range(n - 1):
            next_element = p[-1] + q[i]
            p.append(next_element)

        seen = set()
        for x in p:
            if x < 1 or x > n or x in seen:
                valid = False
                break
            seen.add(x)

        if valid and len(seen) == n:
            print(*p)
            return

    print(-1)

solve()