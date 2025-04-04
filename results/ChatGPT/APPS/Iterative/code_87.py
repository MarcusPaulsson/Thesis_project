def max_projects(n, r, projects):
    # Sort projects based on their required rating and then by rating change
    projects.sort(key=lambda x: (x[0], x[1]))

    # Track the number of projects completed
    completed_projects = 0

    # To keep track of the current rating
    current_rating = r

    # While we can still complete projects
    while True:
        completed_this_round = 0
        for a, b in projects:
            if current_rating >= a:  # Check if we can complete this project
                new_rating = current_rating + b
                if new_rating >= 0:  # Check if completing it keeps rating non-negative
                    current_rating = new_rating
                    completed_projects += 1
                    completed_this_round += 1

        # If no projects were completed in this round, break the loop
        if completed_this_round == 0:
            break

    return completed_projects


# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_projects(n, r, projects)
print(result)