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
            
    result = []
    count = 0
    
    while q:
        u = q.popleft()
        result.append(u)
        count += 1
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
                
    if count != n:
        print("-1")
        return
        
    
    def find_path(start, end, dependencies):
      q = deque([(start, [start])])
      visited = set()

      while q:
          node, path = q.popleft()
          if node == end:
              return path

          visited.add(node)

          for i in range(1,n+1):
              if i not in adj[node]:
                  continue
              
              neighbor = i
              if neighbor not in visited:
                  q.append((neighbor, path + [neighbor]))

      return None

    
    required_courses = set(main_courses)
    
    for i in range(1, n + 1):
        if i in main_courses:
            continue
        
        path_to_main = False
        for main_course in main_courses:
            path = find_path(i, main_course, dependencies)
            if path:
                path_to_main = True
                break
        
        if path_to_main:
            required_courses.add(i)
    
    
    in_degree = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    
    for i in range(n):
        for dep in dependencies[i]:
            if i+1 in required_courses and dep in required_courses:
                adj[dep].append(i + 1)
                in_degree[i + 1] += 1
    
    q = deque()
    for i in required_courses:
        if in_degree[i] == 0:
            q.append(i)
            
    result = []
    count = 0
    
    while q:
        u = q.popleft()
        result.append(u)
        count += 1
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
                
    if count != len(required_courses):
        print("-1")
        return
        
    print(len(result))
    print(*result)
    

solve()