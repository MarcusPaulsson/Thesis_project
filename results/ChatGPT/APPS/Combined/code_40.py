def determine_round_rating(n, ratings):
    # Check if any rating has changed
    for a, b in ratings:
        if a != b:
            return "rated"
    
    # Check if the ratings are in non-increasing order
    for i in range(n - 1):
        if ratings[i][0] < ratings[i + 1][0]:
            return "unrated"
    
    return "maybe"

# Input reading
n = int(input())
ratings = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(determine_round_rating(n, ratings))