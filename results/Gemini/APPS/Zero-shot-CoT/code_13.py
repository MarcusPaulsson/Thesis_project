from collections import deque

def solve():
    n, k = map(int, input().split())
    main_courses = set(map(int, input().split()))
    dependencies = []
    for _ in range(n):
        line = list(map(int, input().split()))
        dependencies.append(line[1:])

    indegree = [0] * n
    adj = [[] for _ in range(n)]
    for i in range(n):
        for dep in dependencies[i]:
            adj[dep - 1].append(i)
            indegree[i] += 1

    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    
    result = []
    visited = [False] * n
    main_courses_reached = set()

    while q:
        u = q.popleft()
        result.append(u + 1)
        visited[u] = True

        if u + 1 in main_courses:
            main_courses_reached.add(u + 1)

        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if len(result) != n:
        print("-1")
        return

    
    required_courses = set()
    q = deque()
    for course in main_courses:
        q.append(course - 1)
        required_courses.add(course - 1)

    while q:
        u = q.popleft()
        for dep in dependencies[u]:
            if dep - 1 not in required_courses:
                required_courses.add(dep - 1)
                q.append(dep - 1)
                

    
    ans = []
    indegree = [0] * n
    adj = [[] for _ in range(n)]
    for i in range(n):
       
        for dep in dependencies[i]:
            if (i in required_courses) and (dep-1 in required_courses):
                adj[dep - 1].append(i)
                indegree[i] += 1
    
    q = deque()
    for i in range(n):
        if indegree[i] == 0 and (i in required_courses):
            q.append(i)
    
    while q:
        u = q.popleft()
        ans.append(u + 1)
        
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
                
    if len(ans) != len(required_courses):
        print("-1")
        return
    
    print(len(ans))
    print(*ans)
    

solve()