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
    
    place_higher_lower_rating = False
    for i in range(n - 1):
        for j in range(i + 1, n):
            if ratings[i][0] < ratings[j][0]:
                place_higher_lower_rating = True
                break
        if place_higher_lower_rating:
            break
    
    if place_higher_lower_rating:
        print("unrated")
        return
    
    print("maybe")

solve()