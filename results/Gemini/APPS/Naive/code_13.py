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
        for dependency in dependencies[i]:
            adj[dependency].append(i + 1)
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

    
    required_courses = set(main_courses)
    
    reachable = [False] * (n + 1)
    q = deque(main_courses)
    for course in main_courses:
        reachable[course] = True
    
    while q:
        u = q.popleft()
        for i in range(1, n + 1):
            if u in adj[i]:
                if not reachable[i]:
                    reachable[i] = True
                    q.append(i)
                    required_courses.add(i)
    
    
    result = []
    visited = [False] * (n + 1)
    
    def dfs(course):
        if visited[course]:
            return True
        
        visited[course] = True
        
        for dependency in dependencies[course-1]:
            if not dfs(dependency):
                return False
        
        result.append(course)
        return True
    
    
    for course in main_courses:
        if not dfs(course):
            print("-1")
            return
            
    final_result = []
    for course in reversed(result):
        if course not in final_result:
            final_result.append(course)
            
    print(len(final_result))
    print(*final_result)

solve()