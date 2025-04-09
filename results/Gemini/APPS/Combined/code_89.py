def solve():
    n, r = map(int, input().split())
    positive_projects = []
    negative_projects = []
    for _ in range(n):
        a, b = map(int, input().split())
        if b >= 0:
            positive_projects.append((a, b))
        else:
            negative_projects.append((a, b))

    positive_projects.sort()
    
    possible = True
    for a, b in positive_projects:
        if r < a:
            possible = False
            break
        r += b

    if not possible:
        print("NO")
        return

    negative_projects.sort(key=lambda x: x[0] + x[1], reverse=True)
    
    for a, b in negative_projects:
        if r < a:
            possible = False
            break
        r += b
        if r < 0:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")

solve()