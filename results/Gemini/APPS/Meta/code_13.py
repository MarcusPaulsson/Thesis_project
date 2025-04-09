from collections import deque

def solve():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    dependencies = []
    for _ in range(n):
        line = list(map(int, input().split()))
        dependencies.append(line[1:])

    in_degree = [0] * n
    adj = [[] for _ in range(n)]
    for i in range(n):
        for dep in dependencies[i]:
            adj[dep - 1].append(i)
            in_degree[i] += 1

    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)

    result = []
    count = 0
    
    necessary = [False] * n
    for course in main_courses:
        necessary[course - 1] = True

    
    q_necessary = deque()
    for i in range(n):
      if necessary[i] and in_degree[i] == 0:
        q_necessary.append(i)
    
    visited = [False] * n
    
    def bfs(start_nodes):
      nonlocal count
      q_local = deque(start_nodes)
      
      while q_local:
        u = q_local.popleft()
        
        if visited[u]:
          continue
        visited[u] = True
        
        result.append(u + 1)
        count += 1
        
        for v in adj[u]:
          in_degree[v] -= 1
          if in_degree[v] == 0:
            q_local.append(v)
    
    
    bfs([i for i in range(n) if in_degree[i] == 0 and i not in [course -1 for course in main_courses]])
    
    
    
    def find_necessary_dependencies(course_index, visited_local):
      deps = []
      for i in range(n):
        for dep in dependencies[i]:
          if dep - 1 == course_index:
            deps.append(i)
      return deps
    
    
    
    def bfs_necessary(start_nodes):
      nonlocal count
      q_local = deque(start_nodes)
      
      while q_local:
        u = q_local.popleft()
        
        if visited[u]:
          continue
        visited[u] = True
        
        result.append(u + 1)
        count += 1
        
        for v in adj[u]:
          in_degree[v] -= 1
          if in_degree[v] == 0:
            q_local.append(v)
            
    
    start_nodes_necessary = []
    for course in main_courses:
      node_index = course - 1
      q = deque([node_index])
      visited_local = [False] * n
      
      while q:
        curr = q.popleft()
        if visited_local[curr]:
          continue
        
        visited_local[curr] = True
        
        if in_degree[curr] != 0:
          start_nodes_necessary.append(curr)
        else:
          start_nodes_necessary.append(curr)
          
        for dep in dependencies[curr]:
              if not visited_local[dep - 1]:
                q.append(dep - 1)
    
    start_nodes_necessary = list(set(start_nodes_necessary))
    
    
    bfs_necessary([i for i in range(n) if necessary[i] and i not in [course - 1 for course in main_courses] and in_degree[i] == 0 and i in start_nodes_necessary])
    bfs_necessary([i for i in range(n) if i in [course - 1 for course in main_courses] and in_degree[i] == 0 and i in start_nodes_necessary])
    

    
    
    if len(result) < len(set(main_courses)):
      print("-1")
      return
    
    
    for course in main_courses:
      if course not in result:
        print("-1")
        return
        
    if count < len(set(main_courses)):
      print("-1")
      return

    if count < len(main_courses):
      print("-1")
      return

    
    
    
    visited_all = [False] * n
    
    def bfs_check(start_nodes):
      q_local = deque(start_nodes)
      
      while q_local:
        u = q_local.popleft()
        
        if visited_all[u]:
          continue
        visited_all[u] = True
        
        for v in adj[u]:
          q_local.append(v)
          
    bfs_check([i for i in range(n) if in_degree[i] == 0])
    
    for course in main_courses:
      if not visited_all[course - 1]:
        print("-1")
        return

    print(len(result))
    print(*result)

solve()