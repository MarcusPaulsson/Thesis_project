def can_complete_projects(n, r, projects):
    # Sort projects by their required rating, secondary sort by rating change
    projects.sort(key=lambda x: (x[0], -x[1]))

    for a, b in projects:
        if r < a:
            return "NO"
        r += b
        if r < 0:
            return "NO"

    return "YES"

n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]
print(can_complete_projects(n, r, projects))