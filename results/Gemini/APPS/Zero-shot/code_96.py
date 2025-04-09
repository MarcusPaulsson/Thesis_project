def solve():
    n = int(input())
    q = list(map(int, input().split()))

    for first_element in range(1, n + 1):
        p = [first_element]
        
        valid = True
        for i in range(n - 1):
            next_element = p[-1] + q[i]
            if 1 <= next_element <= n:
                p.append(next_element)
            else:
                valid = False
                break

        if valid:
            if len(set(p)) == n:
                print(*p)
                return

    print(-1)

solve()