def determine_round_status(n, ratings):
    # Check if any rating has changed
    rated = any(before != after for before, after in ratings)
    
    # Check if standings are in non-increasing order based on the initial ratings
    unrated = any(ratings[i][0] < ratings[i + 1][0] for i in range(n - 1))

    if rated:
        return "rated"
    elif unrated:
        return "unrated"
    else:
        return "maybe"

# Input reading
n = int(input().strip())
ratings = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Determine and print the result
result = determine_round_status(n, ratings)
print(result)