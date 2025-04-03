def can_complete_projects(n, r, projects):
    projects.sort(key=lambda x: x[0])  # Sort projects by required rating

    for a, b in projects:
        if r < a:  # If current rating is less than required for the project
            return "NO"
        r += b  # Update rating after completing the project
        if r < 0:  # Rating should not fall below zero
            return "NO"
    
    return "YES"

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output result
print(can_complete_projects(n, r, projects))