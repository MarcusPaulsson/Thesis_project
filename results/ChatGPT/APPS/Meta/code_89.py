def can_complete_projects(n, r, projects):
    # Sort projects based on the required rating (a_i)
    projects.sort(key=lambda x: x[0])
    
    for a, b in projects:
        if r < a:  # If current rating is less than required for the project
            return "NO"
        r += b  # Update rating after completing the project
        if r < 0:  # If rating goes below zero
            return "NO"
    
    return "YES"

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(can_complete_projects(n, r, projects))