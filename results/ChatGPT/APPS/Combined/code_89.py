def can_complete_projects(n, r, projects):
    # Sort projects by their required rating (a_i)
    projects.sort(key=lambda x: x[0])
    
    for a, b in projects:
        if r < a:
            return "NO"
        r += b
        if r < 0:
            return "NO"
    
    return "YES"

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(can_complete_projects(n, r, projects))