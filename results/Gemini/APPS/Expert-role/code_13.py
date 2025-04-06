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

    order = []
    visited = [False] * n
    
    def check_main_courses(current_order):
        main_courses_passed = set()
        for course in current_order:
            if course + 1 in main_courses:
                main_courses_passed.add(course + 1)
        return len(main_courses_passed) == k

    def find_path():
        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append([i])

        min_len = float('inf')
        best_path = None

        while q:
            path = q.popleft()
            last_node = path[-1]
            
            if check_main_courses(path):
                if len(path) < min_len:
                    min_len = len(path)
                    best_path = path
            
            for neighbor in adj[last_node]:
                if neighbor not in path:
                    new_path = path + [neighbor]
                    q.append(new_path)
        
        if best_path is None:
            return None
        else:
            return best_path
    
    
    def topological_sort():
        q = deque()
        indegree = in_degree[:]
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        count = 0
        top_order = []

        while q:
            u = q.popleft()
            top_order.append(u)
            count += 1

            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        if count != n:
            return None
        else:
            return top_order
            
    
    
    
    
    def find_min_courses():
        
        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append([i])
        
        min_len = float('inf')
        best_path = None
        
        while q:
            path = q.popleft()
            
            main_courses_passed = set()
            for course in path:
                if course + 1 in main_courses:
                    main_courses_passed.add(course + 1)
            
            if len(main_courses_passed) == k:
                if len(path) < min_len:
                    min_len = len(path)
                    best_path = path
            
            last_node = path[-1]
            for neighbor in adj[last_node]:
                if neighbor not in path:
                    new_path = path + [neighbor]
                    q.append(new_path)
        
        return best_path
    
    
    result_path = find_min_courses() 
    
    if result_path is None:
        print("-1")
    else:
        print(len(result_path))
        print(*[x + 1 for x in result_path])

solve()