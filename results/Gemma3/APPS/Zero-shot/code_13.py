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
    passed_main = set()
    
    while queue:
        node = queue.pop(0)
        result.append(node)
        
        if node in main_courses:
            passed_main.add(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(passed_main) != k:
        print(-1)
        return
    
    print(len(result))
    print(*result)

solve()