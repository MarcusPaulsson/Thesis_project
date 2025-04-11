from collections import deque

def solve():
    n, k = map(int, input().split())
    main_courses = set(map(int, input().split()))
    dependencies = []
    in_degree = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        t = line[0]
        deps = line[1:]
        dependencies.append(deps)
        for dep in deps:
            adj[dep].append(i)
            in_degree[i] += 1

    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    order = []
    count = 0
    
    while q:
        u = q.popleft()
        order.append(u)
        count += 1

        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if count != n:
        print("-1")
        return

    
    required_courses = set(main_courses)
    result = []
    visited = [False] * (n + 1)

    def dfs(course):
        if visited[course]:
            return
        visited[course] = True
        for dep in dependencies[course - 1]:
            if not visited[dep]:
                dfs(dep)
        result.append(course)
    
    for course in main_courses:
        if not visited[course]:
            dfs(course)
    
    result.reverse()
    
    final_result = []
    final_visited = [False] * (n + 1)
    
    def dfs2(course):
        if final_visited[course]:
            return
        final_visited[course] = True
        for dep in dependencies[course - 1]:
            if not final_visited[dep]:
                dfs2(dep)
        final_result.append(course)
    
    for course in main_courses:
        if not final_visited[course]:
            dfs2(course)
            
    final_result.reverse()
    
    print(len(final_result))
    print(*final_result)

solve()