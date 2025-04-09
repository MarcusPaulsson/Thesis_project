def max_projects(n, r, projects):
    # Sort projects based on the required rating (a_i)
    projects.sort(key=lambda x: x[0])
    max_count = 0
    current_rating = r

    for a_i, b_i in projects:
        if current_rating >= a_i:
            max_count += 1
            current_rating += b_i
            # Ensure rating does not fall below zero
            if current_rating < 0:
                break

    return max_count

# Read input
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = max_projects(n, r, projects)
print(result)