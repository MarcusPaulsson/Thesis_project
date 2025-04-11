def max_projects(n, r, projects):
    # Sort projects by required rating, then by rating change descending
    projects.sort(key=lambda x: (x[0], -x[1]))
    completed = 0

    while True:
        progress = False
        for i in range(len(projects)):
            a, b = projects[i]
            if r >= a:  # Can complete this project
                r += b  # Update rating
                completed += 1
                projects[i] = (float('inf'), 0)  # Mark as completed
                progress = True
                break  # Restart from the beginning
        if not progress:
            break  # No more projects can be completed

    return completed

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_projects(n, r, projects)
print(result)