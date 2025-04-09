def max_projects(n, r, projects):
    # Sort projects based on the required rating and then by the rating change
    projects.sort(key=lambda x: (x[0], x[1]))

    max_count = 0
    current_rating = r

    # Try to complete as many projects as possible
    for _ in range(n):
        count = 0
        temp_rating = current_rating
        completed_projects = []

        for a_i, b_i in projects:
            if temp_rating >= a_i:
                completed_projects.append((a_i, b_i))
                temp_rating += b_i
                if temp_rating < 0:  # Rating can't go below zero
                    break
                count += 1
        
        max_count = max(max_count, count)

        # Remove completed projects from the list for future iterations
        projects = [p for p in projects if p not in completed_projects]

    return max_count

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_projects(n, r, projects))