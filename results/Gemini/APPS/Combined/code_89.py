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
    negative_projects.sort(key=lambda x: x[0] + x[1], reverse=True)

    def check_projects(projects):
        nonlocal r
        initial_r = r
        for a, b in projects:
            if r < a:
                r = initial_r
                return False
            r += b
            if r < 0:
                r = initial_r
                return False
        return True

    if check_projects(positive_projects) and check_projects(negative_projects):
        print("YES")
    else:
        print("NO")

solve()