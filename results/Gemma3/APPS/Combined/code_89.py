def solve():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    
    import itertools
    
    for perm in itertools.permutations(projects):
        current_rating = r
        possible = True
        for a, b in perm:
            if current_rating < a:
                possible = False
                break
            current_rating += b
            if current_rating < 0:
                possible = False
                break
        if possible:
            print("YES")
            return
    
    print("NO")

solve()