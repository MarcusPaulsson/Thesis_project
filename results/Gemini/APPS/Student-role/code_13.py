from collections import deque

def solve():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    dependencies = []
    for _ in range(n):
        dependencies.append(list(map(int, input().split()))[1:])

    in_degree = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for i in range(n):
        for dep in dependencies[i]:
            adj[dep].append(i + 1)
            in_degree[i + 1] += 1

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

    
    required = set(main_courses)
    result = []
    visited = [False] * (n + 1)
    
    def dfs(course):
        if visited[course]:
            return
        visited[course] = True
        for dep in dependencies[course-1]:
            if not visited[dep]:
                dfs(dep)
        result.append(course)

    for course in main_courses:
        if not visited[course]:
            dfs(course)
    
    result.reverse()
    
    
    
    
    print(len(result))
    print(*result)

solve()