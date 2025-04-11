def determine_round_rating(n, ratings):
    rated = False
    unrated = False
    
    for i in range(n):
        if ratings[i][0] != ratings[i][1]:
            rated = True
            break
    
    if rated:
        print("rated")
        return
    
    for i in range(n - 1):
        if ratings[i][0] < ratings[i + 1][0]:
            unrated = True
            break
    
    if unrated:
        print("unrated")
    else:
        print("maybe")

# Input reading
n = int(input())
ratings = [tuple(map(int, input().split())) for _ in range(n)]
determine_round_rating(n, ratings)