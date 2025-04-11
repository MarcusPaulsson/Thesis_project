def max_projects(n, r, projects):
    # Sort projects based on the required rating and then by the rating change
    projects.sort(key=lambda x: (x[0], x[1]))

    count = 0
    current_rating = r
    completed_projects = []

    for a, b in projects:
        if current_rating >= a:
            completed_projects.append((a, b))
            current_rating += b
            if current_rating < 0:
                break
            count += 1

    return count

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_projects(n, r, projects))