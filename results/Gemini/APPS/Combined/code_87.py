def solve():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))

    pos_projects = []
    neg_projects = []
    for a, b in projects:
        if b >= 0:
            pos_projects.append((a, b))
        else:
            neg_projects.append((a, b))

    pos_projects.sort()
    neg_projects.sort(key=lambda x: x[0] + x[1], reverse=True)

    count = 0
    
    # Process positive projects
    for a, b in pos_projects:
        if r >= a:
            r += b
            count += 1
        
    # Process negative projects
    
    def solve_neg(r, neg_projects):
        n = len(neg_projects)
        dp = {}

        def get_max_projects(current_rating, index):
            if index == n:
                return 0

            key = (current_rating, index)
            if key in dp:
                return dp[key]

            max_count = 0

            # Option 1: Skip the current project
            max_count = max(max_count, get_max_projects(current_rating, index + 1))

            # Option 2: Take the current project if possible
            a, b = neg_projects[index]
            if current_rating >= a and current_rating + b >= 0:
                max_count = max(max_count, 1 + get_max_projects(current_rating + b, index + 1))

            dp[key] = max_count
            return max_count

        return get_max_projects(r, 0)

    count += solve_neg(r, neg_projects)

    print(count)

solve()