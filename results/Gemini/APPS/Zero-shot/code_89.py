def solve():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))

    def check(order):
        rating = r
        for i in order:
            a, b = projects[i]
            if rating < a:
                return False
            rating += b
            if rating < 0:
                return False
        return True

    import itertools
    for perm in itertools.permutations(range(n)):
        if check(perm):
            print("YES")
            return
    print("NO")

solve()