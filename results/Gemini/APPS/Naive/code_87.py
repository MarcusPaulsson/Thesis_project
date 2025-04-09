def solve():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))

    def check(subset):
        pos = []
        neg = []
        for i in subset:
            if projects[i][1] >= 0:
                pos.append(i)
            else:
                neg.append(i)

        pos.sort(key=lambda x: projects[x][0])
        neg.sort(key=lambda x: projects[x][0] + projects[x][1], reverse=True)

        current_rating = r
        
        for i in pos:
            if current_rating >= projects[i][0]:
                current_rating += projects[i][1]
            else:
                return False
        
        for i in neg:
            if current_rating >= projects[i][0]:
                current_rating += projects[i][1]
                if current_rating < 0:
                    return False
            else:
                return False
        
        if current_rating < 0:
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