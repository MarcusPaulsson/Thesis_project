def max_projects(n, r, projects):
    # Sort projects by their required rating
    projects.sort(key=lambda x: x[0])
    
    completed_projects = 0
    current_rating = r
    
    for required_rating, rating_change in projects:
        if current_rating >= required_rating:
            completed_projects += 1
            current_rating += rating_change
            # Ensure the rating does not fall below zero
            if current_rating < 0:
                break
    
    return completed_projects

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_projects(n, r, projects))