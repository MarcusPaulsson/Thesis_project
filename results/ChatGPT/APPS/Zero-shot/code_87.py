def max_projects(n, r, projects):
    projects.sort(key=lambda x: (x[0], -x[1]))  # Sort by required rating, then by rating change
    completed = 0
    
    while True:
        progress = False
        for i in range(len(projects)):
            a_i, b_i = projects[i]
            if r >= a_i:  # Can complete this project
                r += b_i  # Update rating
                completed += 1
                projects[i] = (float('inf'), 0)  # Mark as completed
                progress = True
                break  # Restart the loop to check from the beginning
        if not progress:
            break  # No more projects can be completed
    
    return completed

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_projects(n, r, projects))