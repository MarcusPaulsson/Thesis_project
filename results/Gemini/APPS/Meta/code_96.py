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

    def find_permutation():
        for first_element in range(1, n + 1):
            p = [first_element]
            valid = True
            for i in range(n - 1):
                next_element = p[-1] + q[i]
                p.append(next_element)
            
            if check_permutation(p):
                if len(set(p)) == n and all(1 <= x <= n for x in p):
                    return p
        return None

    result = find_permutation()

    if result is None:
        print("-1")
    else:
        print(*result)

solve()