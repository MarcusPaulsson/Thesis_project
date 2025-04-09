def max_projects(n, r, projects):
    projects.sort(key=lambda x: (x[0], -x[1]))  # Sort projects by required rating, then by rating change descending
    completed = 0
    
    while True:
        progress = False
        for i in range(len(projects)):
            a, b = projects[i]
            if a <= r:  # If current rating is enough to start the project
                if r + b >= 0:  # After completing the project, rating must not drop below zero
                    r += b
                    completed += 1
                    projects[i] = (float('inf'), 0)  # Mark project as completed
                    progress = True
        if not progress:  # No more projects can be completed
            break
            
    return completed

# Input reading section
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_projects(n, r, projects))