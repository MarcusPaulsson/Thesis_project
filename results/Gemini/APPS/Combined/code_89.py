def solve():
    n, r = map(int, input().split())
    positive_projects = []
    negative_projects = []
    for _ in range(n):
        a, b = map(int, input().split())
        if b >= 0:
            positive_projects.append((a, b))
        else:
            negative_projects.append((a, b))

    positive_projects.sort()
    negative_projects.sort(key=lambda x: x[0] + x[1], reverse=True)

    current_rating = r
    for a, b in positive_projects:
        if current_rating < a:
            print("NO")
            return
        current_rating += b

    for a, b in negative_projects:
        if current_rating < a:
            print("NO")
            return
        current_rating += b
        if current_rating < 0:
            print("NO")
            return

    print("YES")

solve()