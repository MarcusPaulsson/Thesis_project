def can_complete_projects(n, r, projects):
    # Sort projects by their required rating (a_i)
    projects.sort()

    for a_i, b_i in projects:
        if r < a_i:  # If current rating is less than required for the project
            return "NO"
        r += b_i  # Update the rating after completing the project
        if r < 0:  # If rating drops below zero
            return "NO"

    return "YES"

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output result
print(can_complete_projects(n, r, projects))