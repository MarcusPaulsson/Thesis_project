def can_complete_projects(n, r, projects):
    projects.sort(key=lambda x: (x[0], -x[1]))  # Sort by required rating, then by rating change descending
    current_rating = r
    
    for a, b in projects:
        if current_rating < a:
            return "NO"
        current_rating += b
        if current_rating < 0:
            return "NO"
    
    return "YES"

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output result
print(can_complete_projects(n, r, projects))