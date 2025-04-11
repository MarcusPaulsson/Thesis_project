def determine_round_rating(n, ratings):
    # Check if any participant's rating has changed
    for before, after in ratings:
        if before != after:
            return "rated"
    
    # Check if the standings are in non-increasing order of ratings
    for i in range(1, n):
        if ratings[i-1][0] < ratings[i][0]:
            return "unrated"
    
    return "maybe"

# Read input
n = int(input())
ratings = [tuple(map(int, input().split())) for _ in range(n)]

# Determine and print the result
print(determine_round_rating(n, ratings))