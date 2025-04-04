def max_projects(n, r, projects):
    # Sort projects by the required rating a_i
    projects.sort(key=lambda x: x[0])
    
    completed_projects = 0
    current_rating = r
    
    for a_i, b_i in projects:
        if current_rating >= a_i:
            completed_projects += 1
            current_rating += b_i
            # Ensure rating does not go below zero
            if current_rating < 0:
                break

    return completed_projects

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_projects(n, r, projects))