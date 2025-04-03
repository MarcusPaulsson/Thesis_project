def max_projects(n, r, projects):
    # Sort projects by their required rating a_i
    projects.sort(key=lambda x: x[0])
    
    count = 0
    current_rating = r
    
    for a, b in projects:
        if current_rating >= a:  # Check if Polycarp can start the project
            count += 1  # Increment the count of projects
            current_rating += b  # Update the rating after completing the project
            if current_rating < 0:  # Ensure rating does not drop below zero
                current_rating = 0
    
    return count

# Read input
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_projects(n, r, projects)
print(result)