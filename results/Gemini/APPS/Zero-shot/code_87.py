def solve():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))

    def check(subset):
        
        pos_projects = []
        neg_projects = []
        for i in subset:
            if projects[i][1] >= 0:
                pos_projects.append(i)
            else:
                neg_projects.append(i)

        
        pos_projects.sort(key=lambda x: projects[x][0])
        neg_projects.sort(key=lambda x: projects[x][0] + projects[x][1], reverse=True)

        
        current_rating = r
        
        for i in pos_projects:
            if current_rating >= projects[i][0]:
                current_rating += projects[i][1]
            else:
                return False

        for i in neg_projects:
            if current_rating >= projects[i][0]:
                current_rating += projects[i][1]
                if current_rating < 0:
                    return False
            else:
                return False
        
        return True

    max_size = 0
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(j)
        
        if check(subset):
            max_size = max(max_size, len(subset))

    print(max_size)

solve()