def max_projects(n, r, projects):
    projects.sort(key=lambda x: (x[0], x[1]))  # Sort by required rating first, then by rating change
    completed = 0
    current_rating = r
    
    while True:
        progress_made = False
        for i in range(len(projects)):
            a_i, b_i = projects[i]
            if a_i <= current_rating:  # Can complete this project
                new_rating = current_rating + b_i
                if new_rating >= 0:  # Ensure rating does not fall below zero
                    current_rating = new_rating
                    completed += 1
                    projects[i] = (float('inf'), 0)  # Mark as completed
                    progress_made = True
        if not progress_made:  # No more projects can be completed
            break

    return completed

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_projects(n, r, projects))