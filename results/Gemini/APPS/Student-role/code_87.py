def solve():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))

    def can_complete(subset, order, initial_rating):
        rating = initial_rating
        for project_index in order:
            a, b = subset[project_index]
            if rating < a:
                return False
            rating += b
            if rating < 0:
                return False
        return True

    def find_max_subset(projects, initial_rating):
        max_size = 0
        for i in range(1 << n):
            subset = []
            indices = []
            for j in range(n):
                if (i >> j) & 1:
                    subset.append(projects[j])
                    indices.append(j)

            if not subset:
                max_size = max(max_size, 0)
                continue

            import itertools
            
            valid_subset = False
            for permutation in itertools.permutations(range(len(subset))):
                order = []
                for index in permutation:
                    order.append(indices[index])
                
                if can_complete(projects, order, initial_rating):
                    max_size = max(max_size, len(subset))
                    valid_subset = True
                    break
            
            if not valid_subset and len(subset) > 0 and max_size < len(subset):
                pass
        return max_size

    print(find_max_subset(projects, r))

solve()