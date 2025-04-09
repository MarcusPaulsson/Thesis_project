def can_complete_projects(n, r, projects):
    # Sort projects by required rating (a_i) in ascending order
    projects.sort(key=lambda x: x[0])
    
    for a_i, b_i in projects:
        if r < a_i:  # Not enough rating to start the project
            return "NO"
        r += b_i  # Update rating after completing the project
        if r < 0:  # Rating should not fall below zero
            return "NO"
    
    return "YES"

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(can_complete_projects(n, r, projects))