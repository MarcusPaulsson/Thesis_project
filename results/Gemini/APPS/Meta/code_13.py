from collections import deque

def solve():
    n, k = map(int, input().split())
    main_courses = set(map(int, input().split()))
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
    visited = [False] * (n + 1)
    
    while q:
        u = q.popleft()
        order.append(u)
        visited[u] = True
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
                
    if len(order) != n:
        print("-1")
        return
    
    
    required_courses = set(main_courses)
    
    result = []
    
    for course in order:
        if course in required_courses or all(dep in result for dep in dependencies[course-1]):
            result.append(course)
            if course in main_courses:
                required_courses.remove(course)
    
    if len(required_courses) > 0:
        print("-1")
        return
    
    print(len(result))
    print(*result)

solve()