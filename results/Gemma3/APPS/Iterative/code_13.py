def solve():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    dependencies = []
    for _ in range(n):
        dependencies.append(list(map(int, input().split())))
    
    in_degree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    for i in range(n):
        for dependency in dependencies[i][1:]:
            graph[dependency].append(i + 1)
            in_degree[i + 1] += 1
    
    queue = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    result = []
    passed_main = [False] * k
    
    while queue:
        course = queue.pop(0)
        result.append(course)
        
        for i in range(k):
            if main_courses[i] == course:
                passed_main[i] = True
        
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if not all(passed_main):
        print(-1)
        return
    
    print(len(result))
    print(*result)

solve()