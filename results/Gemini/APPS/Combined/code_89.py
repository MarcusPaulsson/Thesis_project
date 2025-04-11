def solve():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))

    positive_projects = []
    negative_projects = []
    for a, b in projects:
        if b >= 0:
            positive_projects.append((a, b))
        else:
            negative_projects.append((a, b))

    positive_projects.sort()
    
    for a, b in positive_projects:
        if r >= a:
            r += b
        else:
            print("NO")
            return

    negative_projects.sort(key=lambda x: x[0] + x[1], reverse=True)

    for a, b in negative_projects:
        if r >= a:
            r += b
            if r < 0:
                print("NO")
                return
        else:
            print("NO")
            return

    print("YES")

solve()