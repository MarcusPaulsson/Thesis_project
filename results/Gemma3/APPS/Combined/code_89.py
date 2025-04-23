def solve():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    
    import itertools
    
    for perm in itertools.permutations(projects):
        curr_r = r
        possible = True
        for a, b in perm:
            if curr_r < a:
                possible = False
                break
            curr_r += b
            if curr_r < 0:
                possible = False
                break
        if possible:
            print("YES")
            return
    
    print("NO")

solve()