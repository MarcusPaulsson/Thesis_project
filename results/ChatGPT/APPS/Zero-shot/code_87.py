def max_projects(n, r, projects):
    # Sort projects based on required rating
    projects.sort()
    
    completed = 0
    current_rating = r
    
    while True:
        progress = False
        for i in range(len(projects)):
            a, b = projects[i]
            if a <= current_rating:
                current_rating += b
                # If current rating drops below zero, skip this project
                if current_rating < 0:
                    current_rating -= b  # revert change
                else:
                    completed += 1
                    projects[i] = (float('inf'), 0)  # mark as completed
                    progress = True
                    break
        if not progress:
            break
    
    return completed

# Read input
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and print the maximum possible size of the subset
print(max_projects(n, r, projects))