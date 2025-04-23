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
    
    better_place_higher_rating = False
    for i in range(n):
        for j in range(i + 1, n):
            if ratings[i][0] < ratings[j][0]:
                better_place_higher_rating = True
                break
        if better_place_higher_rating:
            break
    
    if better_place_higher_rating:
        print("unrated")
        return
    
    print("maybe")

solve()