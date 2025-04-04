def can_complete_projects(n, r, projects):
    # Sort projects by the required rating, then by the rating change
    projects.sort(key=lambda x: (x[0], -x[1]))

    for a, b in projects:
        if r < a:  # Not enough rating to start the project
            return "NO"
        r += b  # Update rating after completing the project
        if r < 0:  # Rating should not fall below zero
            return "NO"

    return "YES"

# Read input
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Check if all projects can be completed
result = can_complete_projects(n, r, projects)
print(result)