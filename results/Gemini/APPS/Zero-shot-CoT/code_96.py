def solve():
    n = int(input())
    q = list(map(int, input().split()))

    def check_permutation(p):
        if len(p) != n:
            return False
        if len(set(p)) != n:
            return False
        for x in p:
            if not (1 <= x <= n):
                return False
        return True

    def construct_permutation(first_element):
        p = [first_element]
        for i in range(n - 1):
            p.append(p[-1] + q[i])
        return p

    for first_element in range(1, n + 1):
        p = construct_permutation(first_element)
        if check_permutation(p):
            print(*p)
            return

    print(-1)

solve()