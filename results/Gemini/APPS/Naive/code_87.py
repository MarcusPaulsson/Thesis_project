def solve():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))

    positive_projects = []
    negative_projects = []
    for a, b in projects:
        if b >= 0:
            positive_projects.append((a, b))
        else:
            negative_projects.append((a, b))

    positive_projects.sort()

    count = 0
    for a, b in positive_projects:
        if r >= a:
            r += b
            count += 1

    negative_projects.sort(key=lambda x: x[0] + x[1], reverse=True)

    
    def can_complete(subset):
        current_rating = r
        for a, b in subset:
            if current_rating >= a:
                current_rating += b
                if current_rating < 0:
                    return False
            else:
                return False
        return True

    def find_max_subset(negative_projects_list, current_rating):
        max_size = 0
        
        for i in range(1 << len(negative_projects_list)):
            subset = []
            for j in range(len(negative_projects_list)):
                if (i >> j) & 1:
                    subset.append(negative_projects_list[j])
            
            if can_complete(subset):
                max_size = max(max_size, len(subset))

        return max_size

    print(count + find_max_subset(negative_projects, r))

solve()