def can_complete_projects(n, r, projects):
    # Sort projects based on the required rating 'a_i', and in case of a tie, by 'b_i' descending
    projects.sort(key=lambda x: (x[0], -x[1]))
    
    for a_i, b_i in projects:
        if r < a_i:
            return "NO"
        r += b_i
        if r < 0:
            return "NO"
    
    return "YES"

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(can_complete_projects(n, r, projects))