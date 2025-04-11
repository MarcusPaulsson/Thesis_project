def max_projects(n, r, projects):
    # Sort projects by their required rating
    projects.sort(key=lambda x: x[0])
    
    completed = 0
    current_rating = r
    
    for a, b in projects:
        if current_rating >= a:
            completed += 1
            current_rating += b
            if current_rating < 0:
                break
    
    return completed

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_projects(n, r, projects))