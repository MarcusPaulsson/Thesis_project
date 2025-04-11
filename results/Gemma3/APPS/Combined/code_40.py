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
    
    out_of_order = False
    for i in range(n - 1):
        if ratings[i][0] < ratings[i+1][0]:
            out_of_order = True
            break
    
    if out_of_order:
        print("unrated")
        return
    
    print("maybe")

solve()