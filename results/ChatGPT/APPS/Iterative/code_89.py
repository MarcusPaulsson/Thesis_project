def can_complete_projects(n, r, projects):
    # Sort projects based on their required rating (a_i)
    projects.sort(key=lambda x: x[0])
    
    current_rating = r
    
    for required_rating, rating_change in projects:
        # Check if current rating is sufficient to start the project
        if current_rating < required_rating:
            return "NO"
        # Update current rating after completing the project
        current_rating += rating_change
        # Ensure the rating does not drop below zero
        if current_rating < 0:
            return "NO"
    
    return "YES"

# Input handling
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(can_complete_projects(n, r, projects))