def max_projects(n, r, projects):
    # Sort projects based on the required rating a_i
    projects.sort(key=lambda x: x[0])
    
    count = 0
    current_rating = r
    
    for a_i, b_i in projects:
        if current_rating >= a_i:  # Check if Polycarp can start the project
            count += 1  # Increment the count of projects
            current_rating += b_i  # Update the current rating after completing the project
            if current_rating < 0:  # Ensure rating does not fall below zero
                break
    
    return count

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_projects(n, r, projects))