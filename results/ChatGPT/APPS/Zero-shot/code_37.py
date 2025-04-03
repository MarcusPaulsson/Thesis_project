def max_projects(n, r, projects):
    # Sort projects based on their required rating (a_i)
    projects.sort(key=lambda x: x[0])
    
    # Counter for the maximum number of projects Polycarp can complete
    count = 0
    
    # While there are still projects to consider
    while True:
        completed = False
        for a, b in projects:
            # Check if Polycarp can complete the project
            if r >= a:
                # Complete the project
                r += b
                count += 1
                completed = True
                # If rating goes below 0, we can't continue
                if r < 0:
                    return count
                # Remove the project from the list
                projects.remove((a, b))
                break
        # If no projects were completed in the last iteration, break the loop
        if not completed:
            break
            
    return count

# Read input
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_projects(n, r, projects)
print(result)