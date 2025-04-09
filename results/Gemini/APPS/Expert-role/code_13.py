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
        print(-1)
        return

    
    required_courses = set(main_courses)
    result = []
    passed = set()
    
    def find_path(start_node):
        q = deque([([start_node], {start_node})])
        
        while q:
            path, visited = q.popleft()
            node = path[-1]
            
            if node in required_courses:
                return path
            
            for pred in get_predecessors(node):
                if pred not in visited:
                    new_path = path + [pred]
                    new_visited = visited | {pred}
                    q.append((new_path, new_visited))
        return None
    
    def get_predecessors(node):
        predecessors = []
        for i in range(1, n + 1):
            if node in adj[i]:
                predecessors.append(i)
        return predecessors
    
    
    for course in main_courses:
      
        path = find_path(course)

        if path is None:
            print(-1)
            return
        
        
        for node in reversed(path):
            if node not in passed:
                result.append(node)
                passed.add(node)
    
    
    
    print(len(result))
    print(*result)
    
solve()