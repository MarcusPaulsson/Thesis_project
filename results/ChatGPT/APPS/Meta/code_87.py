def max_projects(n, r, projects):
    # Sort projects based on their required rating
    projects.sort(key=lambda x: (x[0], -x[1]))

    count = 0  # To count the maximum number of projects
    current_rating = r  # Current rating of Polycarp

    for a, b in projects:
        if current_rating >= a:  # Check if the project can be started
            count += 1  # Increment the count of projects
            current_rating += b  # Update the rating after completing the project
            if current_rating < 0:  # If rating goes below 0, break
                break

    return count

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_projects(n, r, projects)
print(result)