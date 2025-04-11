def max_projects(n, r, projects):
    # Sort projects by their required rating
    projects.sort(key=lambda x: x[0])
    
    count = 0
    current_rating = r
    
    # First, complete all projects that can be done without going negative
    for a, b in projects:
        if current_rating >= a:
            current_rating += b
            if current_rating < 0:
                break
            count += 1
            
    # Now we need to check if we can complete more projects by skipping some
    # We will use a greedy approach to try to maximize the number of projects
    completed_projects = []
    
    for a, b in projects:
        if current_rating >= a:
            completed_projects.append((a, b))
            current_rating += b
            
    # If we have completed projects, we can try to complete more by considering negative b values
    completed_projects.sort(key=lambda x: x[1])  # Sort by rating change
    
    for a, b in completed_projects:
        if current_rating >= a:
            current_rating += b
            if current_rating < 0:
                break
            count += 1
            
    return count

# Read input
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_projects(n, r, projects)
print(result)