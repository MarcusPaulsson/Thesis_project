def max_projects(n, r, projects):
    # Sort projects based on their required rating and rating change
    projects.sort(key=lambda x: (x[0], -x[1]))

    completed_projects = 0
    current_rating = r

    while True:
        progress_made = False
        for i in range(len(projects)):
            a_i, b_i = projects[i]
            if current_rating >= a_i:
                # Complete the project
                current_rating += b_i
                completed_projects += 1
                # Remove the project from the list
                projects.pop(i)
                progress_made = True
                break
        if not progress_made:
            break

    return completed_projects

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_projects(n, r, projects))