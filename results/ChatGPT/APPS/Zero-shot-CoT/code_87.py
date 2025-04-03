def max_projects(n, r, projects):
    # Separate the projects into two groups: those that increase rating and those that decrease it
    increase_projects = []
    decrease_projects = []

    for a, b in projects:
        if b >= 0:
            increase_projects.append((a, b))
        else:
            decrease_projects.append((a, b))

    # Sort increasing projects by required rating
    increase_projects.sort()

    # Try to complete all increasing projects first
    current_rating = r
    completed_projects = 0

    for a, b in increase_projects:
        if current_rating >= a:
            current_rating += b
            completed_projects += 1

    # Sort decreasing projects by required rating
    decrease_projects.sort()

    # Try to complete decreasing projects
    while True:
        any_completed = False
        for a, b in decrease_projects:
            if current_rating >= a:
                current_rating += b
                if current_rating < 0:  # If rating drops below zero, we can't complete this project
                    current_rating -= b  # revert the change
                else:
                    completed_projects += 1
                    any_completed = True
        if not any_completed:
            break

    return completed_projects

# Read input
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print
result = max_projects(n, r, projects)
print(result)