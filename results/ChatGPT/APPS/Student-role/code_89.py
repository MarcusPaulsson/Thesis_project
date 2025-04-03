def can_complete_projects(n, r, projects):
    # Sort projects based on the required rating
    projects.sort(key=lambda x: x[0])  # Sort by a_i (required rating)
    
    for a, b in projects:
        if r < a:  # If current rating is less than required rating for the project
            return "NO"
        r += b  # Update rating after completing the project
        if r < 0:  # If rating falls below 0
            return "NO"
    
    return "YES"

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Check if all projects can be completed
result = can_complete_projects(n, r, projects)
print(result)