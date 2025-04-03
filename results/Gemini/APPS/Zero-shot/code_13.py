from collections import deque

def solve():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    dependencies = []
    for _ in range(n):
        line = list(map(int, input().split()))
        dependencies.append(line[1:])

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

    
    q = deque()
    visited = [False] * (n + 1)
    
    for course in main_courses:
        q.append(course)
        visited[course] = True

    result = []

    while q:
        u = q.popleft()
        result.append(u)
        
        for i in range(1, n + 1):
            if i not in result:
                can_add = True
                for dep in dependencies[i-1]:
                    if dep not in result:
                        can_add = False
                        break
                if can_add:
                    if not visited[i]:
                        q.append(i)
                        visited[i] = True

    final_result = []
    visited = [False] * (n + 1)
    
    def dfs(course):
        if visited[course]:
            return
        visited[course] = True
        
        for dep in dependencies[course-1]:
            dfs(dep)
        
        final_result.append(course)

    for course in main_courses:
        if not visited[course]:
            dfs(course)

    result = []
    for i in range(1, n + 1):
        if i in final_result or i in main_courses:
           pass
    
    q = deque()
    visited = [False] * (n + 1)
    
    for course in main_courses:
        q.append(course)
        visited[course] = True

    result = []

    while q:
        u = q.popleft()
        result.append(u)
        
        for i in range(1, n + 1):
            if i not in result:
                can_add = True
                for dep in dependencies[i-1]:
                    if dep not in result:
                        can_add = False
                        break
                if can_add:
                    if not visited[i]:
                        q.append(i)
                        visited[i] = True
    print(len(result))
    print(*result)
    
solve()