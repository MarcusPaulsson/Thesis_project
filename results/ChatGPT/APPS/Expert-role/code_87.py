def max_project_subset(n, r, projects):
    # Sort projects by their required rating a_i
    projects.sort()
    
    count = 0
    current_rating = r
    
    for a_i, b_i in projects:
        if current_rating >= a_i:
            count += 1
            current_rating += b_i
            # Ensure rating does not fall below zero
            if current_rating < 0:
                break
    
    return count

# Read input
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_project_subset(n, r, projects)
print(result)