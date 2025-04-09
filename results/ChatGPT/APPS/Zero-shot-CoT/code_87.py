def max_projects(n, r, projects):
    # Separate projects into those that can increase rating and those that can decrease rating
    can_gain = []
    can_lose = []

    for a, b in projects:
        if b >= 0:
            can_gain.append((a, b))
        else:
            can_lose.append((a, b))

    # Sort projects that can increase rating by their required rating
    can_gain.sort()
    
    # Sort projects that can decrease rating by their required rating
    can_lose.sort()

    # Perform projects that can gain rating
    current_rating = r
    total_completed = 0

    for a, b in can_gain:
        if current_rating >= a:
            current_rating += b
            total_completed += 1

    # Perform projects that can lose rating
    # To do this, we need to sort them and try to complete them in a way that
    # we never go below zero rating.
    for a, b in can_lose:
        if current_rating >= a:
            current_rating += b
            if current_rating >= 0:
                total_completed += 1

    return total_completed

# Input reading
n, r = map(int, input().split())
projects = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
print(max_projects(n, r, projects))