def can_complete_projects(n, r, projects):
    # Sort projects based on the required rating (a_i)
    projects.sort(key=lambda x: x[0])
    
    for a_i, b_i in projects:
        if r < a_i:  # Check if current rating is less than required
            return "NO"
        r += b_i  # Update rating after completing the project
        if r < 0:  # Check if rating goes below zero
            return "NO"
    
    return "YES"

# Input handling
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(can_complete_projects(n, r, projects))