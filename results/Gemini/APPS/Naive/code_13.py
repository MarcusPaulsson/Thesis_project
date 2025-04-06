def solve():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    dependencies = []
    for _ in range(n):
        line = list(map(int, input().split()))
        dependencies.append(line[1:])

    indegree = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for i in range(n):
        for dep in dependencies[i]:
            adj[dep].append(i + 1)
            indegree[i + 1] += 1

    q = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    order = []
    count = 0
    
    while q:
        u = q.pop(0)
        order.append(u)
        count += 1
        
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if count != n:
        print(-1)
        return

    
    required = set(main_courses)
    
    reachable = set()
    
    def dfs(course):
        reachable.add(course)
        for i in range(n):
            if course in dependencies[i]:
                if i + 1 not in reachable:
                    dfs(i+1)

    for course in main_courses:
        dfs(course)
        
    
    
    path = []
    visited = [False] * (n+1)
    
    def find_path(start_nodes):
      
      q = []
      
      for node in start_nodes:
        q.append( ([node],set([node])) )

      shortest_path = None
      
      while q:
        curr_path, visited_nodes = q.pop(0)
        
        last_node = curr_path[-1]
        
        is_complete = True
        for course in main_courses:
          if course not in visited_nodes:
            is_complete = False
            break
            
        if is_complete:
           if shortest_path is None or len(curr_path) < len(shortest_path):
              shortest_path = curr_path
        
        for next_node in adj[last_node]:
          if next_node not in visited_nodes:
            new_path = curr_path + [next_node]
            new_visited_nodes = visited_nodes.copy()
            new_visited_nodes.add(next_node)
            q.append((new_path, new_visited_nodes))
            
      return shortest_path
            
    start_nodes = []
    for i in range(1,n+1):
        if indegree[i] == 0:
            start_nodes.append(i)
            
    
    final_path = find_path(start_nodes)
    
    if final_path is None:
        print(-1)
    else:
        print(len(final_path))
        print(*final_path)
    
solve()