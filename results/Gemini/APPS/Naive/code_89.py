def solve():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))

    def can_complete(order):
        current_rating = r
        for i in order:
            a, b = projects[i]
            if current_rating < a:
                return False
            current_rating += b
            if current_rating < 0:
                return False
        return True

    import itertools
    for order in itertools.permutations(range(n)):
        if can_complete(order):
            print("YES")
            return
    
    print("NO")

solve()