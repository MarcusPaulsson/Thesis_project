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

    def check_projects(projects, initial_rating):
        current_rating = initial_rating
        for a, b in projects:
            if current_rating < a:
                return False
            current_rating += b
            if current_rating < 0:
                return False
        return True

    if not check_projects(positive_projects, r):
        print("NO")
        return

    r += sum(b for a, b in positive_projects)

    if not check_projects(negative_projects, r):
        print("NO")
        return

    print("YES")

solve()