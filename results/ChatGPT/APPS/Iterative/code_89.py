def can_complete_projects(n, r, projects):
    # Sort projects based on the required rating
    projects.sort(key=lambda x: x[0])
    
    for a, b in projects:
        if r < a:  # If current rating is less than required for the project
            return "NO"
        r += b  # Update the rating after completing the project
        if r < 0:  # If rating goes below zero, return "NO"
            return "NO"
    
    return "YES"

# Input reading
try:
    n, r = map(int, input().split())
    if n < 1 or r < 0:
        raise ValueError("Invalid input values for n or r.")
except ValueError as e:
    print(f"Error: {e}")
    exit(1)

projects = []
for _ in range(n):
    try:
        project = tuple(map(int, input().split()))
        if len(project) != 2 or project[0] < 0 or project[1] < -r:
            raise ValueError("Invalid project data.")
        projects.append(project)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

# Output the result
print(can_complete_projects(n, r, projects))