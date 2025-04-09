def max_projects(n, r, projects):
    # Sort projects based on the rating needed to complete them
    projects.sort(key=lambda x: x[0])

    completed_projects = 0
    current_rating = r

    for a, b in projects:
        if current_rating >= a:
            completed_projects += 1
            current_rating += b
            # Ensure rating doesn't fall below zero
            if current_rating < 0:
                current_rating = 0
                
    return completed_projects

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and output the maximum number of projects
print(max_projects(n, r, projects))