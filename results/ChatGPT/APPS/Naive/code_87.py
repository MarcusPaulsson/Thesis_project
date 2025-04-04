def max_projects(n, r, projects):
    # Sort projects based on their required rating
    projects.sort(key=lambda x: x[0])
    
    count = 0
    current_rating = r
    
    # Loop through the sorted projects
    for a, b in projects:
        # Check if current rating is sufficient to take on the project
        if current_rating >= a:
            count += 1
            current_rating += b
            
            # Ensure rating does not fall below zero
            if current_rating < 0:
                break
            
    return count

# Read input values
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Get the maximum number of projects Polycarp can complete
result = max_projects(n, r, projects)
print(result)