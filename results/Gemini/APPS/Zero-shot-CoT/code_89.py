def solve():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))

    def check(order):
        curr_r = r
        for i in order:
            a, b = projects[i]
            if curr_r < a:
                return False
            curr_r += b
            if curr_r < 0:
                return False
        return True

    import itertools
    for order in itertools.permutations(range(n)):
        if check(order):
            print("YES")
            return
    
    print("NO")

solve()