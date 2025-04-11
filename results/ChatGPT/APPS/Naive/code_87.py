def max_projects(n, r, projects):
    # Sort projects by their required rating
    projects.sort(key=lambda x: x[0])
    
    completed_projects = 0
    current_rating = r
    
    for a, b in projects:
        if current_rating >= a:
            completed_projects += 1
            current_rating += b
            if current_rating < 0:
                break
    
    return completed_projects

# Read input
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
result = max_projects(n, r, projects)
print(result)