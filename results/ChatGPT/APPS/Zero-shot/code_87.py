def max_projects(n, r, projects):
    projects.sort(key=lambda x: (x[0], -x[1]))

    completed_projects = 0
    current_rating = r
    
    while True:
        progress = False
        for i in range(len(projects)):
            a_i, b_i = projects[i]
            if a_i <= current_rating:
                if current_rating + b_i >= 0:
                    current_rating += b_i
                    completed_projects += 1
                    projects[i] = (float('inf'), 0)  # Mark as completed
                    progress = True
                    break
        if not progress:
            break
            
    return completed_projects

# Reading input
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Getting the result and printing it
result = max_projects(n, r, projects)
print(result)