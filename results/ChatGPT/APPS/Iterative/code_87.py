def max_projects(n, r, projects):
    # Sort projects: first by required rating, then by rating change (negative changes come last)
    projects.sort(key=lambda x: (x[0], x[1] if x[1] >= 0 else float('inf')))

    completed = 0
    current_rating = r

    for required, change in projects:
        if current_rating >= required:
            completed += 1
            current_rating += change
            if current_rating < 0:
                break  # If rating goes below zero, stop
        # There is no need for an else statement since we just skip to the next project

    return completed

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output result
print(max_projects(n, r, projects))