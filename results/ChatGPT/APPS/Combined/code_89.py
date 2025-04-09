def can_complete_projects(n, initial_rating, projects):
    # Sort projects by their required rating (a_i)
    projects.sort(key=lambda x: x[0])
    
    current_rating = initial_rating
    
    for required_rating, rating_change in projects:
        if current_rating < required_rating:
            return "NO"
        current_rating += rating_change
        if current_rating < 0:
            return "NO"
    
    return "YES"

# Input reading
n, initial_rating = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(can_complete_projects(n, initial_rating, projects))