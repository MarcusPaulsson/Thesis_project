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
            in_degree[i+1] += 1
            
    q = deque()
    for i in range(1, n+1):
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
    
    
    
    
    
    def find_path(start_nodes, adj, n):
        q = deque(start_nodes)
        visited = [False] * (n + 1)
        path = []
        
        for node in start_nodes:
            visited[node] = True
            
        while q:
            u = q.popleft()
            path.append(u)
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        return path, visited
    
    
    
    
    start_nodes = []
    for i in range(1, n+1):
        indegree_count = 0
        for j in range(1, n+1):
            if i in adj[j]:
                indegree_count += 1
        if indegree_count == 0:
            start_nodes.append(i)
    
    
    
    
    
    required_courses = set(main_courses)
    
    
    
    def get_dependencies(course, dependencies):
        deps = []
        for dep in dependencies[course-1]:
            deps.append(dep)
        return deps
    
   
    
    
    def check_if_all_main_courses_present(path, main_courses):
        for course in main_courses:
            if course not in path:
                return False
        return True
    
            
    
    
    
    q = deque()
    
    for i in range(1, n+1):
        if i in main_courses:
            q.append([i, [i]])
            
    
    
    
    best_path = []
    min_len = float('inf')
    
    
    
    
    
    def find_min_courses(start_courses, adj, n, main_courses):
        q = deque()
        visited = [False] * (n + 1)
        
        for course in start_courses:
            q.append([course, [course]])
            visited[course] = True
        
        min_len = float('inf')
        best_path = []
        
        while q:
            curr_course, curr_path = q.popleft()
            
            main_courses_present = 0
            for main_course in main_courses:
                if main_course in curr_path:
                    main_courses_present += 1
            
            if main_courses_present == len(main_courses):
                if len(curr_path) < min_len:
                    min_len = len(curr_path)
                    best_path = curr_path
                continue
            
            
            for neighbor in range(1, n+1):
                if curr_course in dependencies[neighbor-1]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append([neighbor, curr_path + [neighbor]])
        
        return best_path, min_len
    
    
    
    
    
    
    best_path, min_len = find_min_courses(main_courses, adj, n, main_courses)
    
    
    
    
    if len(best_path) == 0:
        print("-1")
        return
        
    
    
    
    
    
    passed_courses = []
    
    
    
    q = deque()
    
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
    
    
    
    
    
    
    
    
    
    
    visited = [False] * (n+1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print(len(best_path))
    print(*best_path)
    
solve()