def solve():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    dependencies = []
    for _ in range(n):
        dependencies.append(list(map(int, input().split())))
    
    in_degree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    for i in range(n):
        if len(dependencies[i]) > 0:
            for dep in dependencies[i]:
                graph[dep].append(i + 1)
                in_degree[i + 1] += 1
    
    queue = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    result = []
    passed_main = [False] * k
    
    while queue:
        u = queue.pop(0)
        result.append(u)
        
        for i in range(k):
            if main_courses[i] == u:
                passed_main[i] = True
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    if all(passed_main):
        print(len(result))
        print(*result)
    else:
        print(-1)

solve()