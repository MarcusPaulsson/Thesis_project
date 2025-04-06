def solve():
    n, r = map(int, input().split())
    pos_projects = []
    neg_projects = []
    for _ in range(n):
        a, b = map(int, input().split())
        if b >= 0:
            pos_projects.append((a, b))
        else:
            neg_projects.append((a, b))

    pos_projects.sort()
    
    curr_rating = r
    for a, b in pos_projects:
        if curr_rating < a:
            print("NO")
            return
        curr_rating += b
    
    neg_projects.sort(key=lambda x: x[0] + x[1], reverse=True)
    
    for a, b in neg_projects:
        if curr_rating < a:
            print("NO")
            return
        curr_rating += b
        if curr_rating < 0:
            print("NO")
            return
            
    print("YES")

solve()