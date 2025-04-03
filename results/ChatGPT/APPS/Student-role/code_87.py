def max_projects(n, r, projects):
    # Sort projects by their required rating
    projects.sort(key=lambda x: (x[0], x[1]))
    
    completed_projects = 0
    current_rating = r
    
    for a, b in projects:
        if current_rating >= a:  # Can attempt this project
            completed_projects += 1
            current_rating += b  # Update current rating after completing the project
            if current_rating < 0:  # If rating falls below zero, stop
                break
    
    return completed_projects

# Read input
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_projects(n, r, projects)
print(result)