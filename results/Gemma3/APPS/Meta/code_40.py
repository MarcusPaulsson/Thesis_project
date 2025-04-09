def solve():
    n = int(input())
    ratings = []
    for _ in range(n):
        a, b = map(int, input().split())
        ratings.append((a, b))
    
    rating_changed = False
    for a, b in ratings:
        if a != b:
            rating_changed = True
            break
    
    if rating_changed:
        print("rated")
        return
    
    place_lower_rating = False
    for i in range(n - 1):
        if ratings[i][0] < ratings[i+1][0]:
            place_lower_rating = True
            break
    
    if place_lower_rating:
        print("unrated")
        return
    
    print("maybe")

solve()