def can_complete_projects(n, r, projects):
    # Sort projects by the rating required in ascending order
    projects.sort(key=lambda x: x[0])
    
    for required_rating, rating_change in projects:
        if r < required_rating:  # Check if current rating is sufficient
            return "NO"
        r += rating_change  # Update rating after project completion
        if r < 0:  # Ensure rating doesn't fall below zero
            return "NO"
    
    return "YES"

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(can_complete_projects(n, r, projects))