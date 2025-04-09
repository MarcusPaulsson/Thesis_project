from collections import deque

def solve():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    dependencies = []
    for _ in range(n):
        dependencies.append(list(map(int, input().split()))[1:])

    indegree = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for i in range(n):
        for dep in dependencies[i]:
            adj[dep].append(i + 1)
            indegree[i + 1] += 1

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    order = []
    count = 0
    
    while q:
        u = q.popleft()
        order.append(u)
        count += 1
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if count != n:
        print(-1)
        return

    
    necessary = set(main_courses)
    for i in range(1,n+1):
      for j in main_courses:
        if j in adj[i]:
          necessary.add(i)

    
    
    
    
    result = []
    visited = [False] * (n+1)
    
    def dfs(node):
        if visited[node]:
            return
        visited[node] = True
        for dep in dependencies[node-1]:
            if not visited[dep]:
                dfs(dep)
        result.append(node)

    for course in main_courses:
        if not visited[course]:
          dfs(course)
    
    
    
    result.reverse()
    
    final_result = []
    seen = set()
    
    for course in result:
      if course not in seen:
        final_result.append(course)
        seen.add(course)

    
    
    
    
    
    
    valid = True
    needed_courses = set(main_courses)
    
    temp_seen = set()
    for course in final_result:
      temp_seen.add(course)
    
    for course in main_courses:
      if course not in temp_seen:
        valid = False
        break
    
    for course in final_result:
      
      
      can_take = True
      
      for dep in dependencies[course-1]:
        if dep not in temp_seen:
          can_take = False
          break
      
      if not can_take:
        valid = False
        break
      
    if not valid:
      print(-1)
      return
        
    
    print(len(final_result))
    print(*final_result)

solve()