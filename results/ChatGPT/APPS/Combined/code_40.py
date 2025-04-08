def determine_round_status(n, ratings):
    # Check if any rating has changed
    if any(before != after for before, after in ratings):
        return "rated"
    
    # Check if ratings are in non-increasing order
    if any(ratings[i][0] < ratings[i + 1][0] for i in range(n - 1)):
        return "unrated"
    
    return "maybe"

# Read input
n = int(input())
ratings = [tuple(map(int, input().split())) for _ in range(n)]

# Determine and print the round status
print(determine_round_status(n, ratings))