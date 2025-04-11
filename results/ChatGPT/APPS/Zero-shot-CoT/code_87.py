def max_projects(n, r, projects):
    projects.sort(key=lambda x: (x[0], -x[1]))  # Sort by required rating, then by rating change
    count = 0
    current_rating = r
    
    for a, b in projects:
        if current_rating >= a:  # Can start the project
            count += 1
            current_rating += b  # Update rating after completing the project
            if current_rating < 0:  # If rating goes below zero, break
                break
    
    return count

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_projects(n, r, projects))