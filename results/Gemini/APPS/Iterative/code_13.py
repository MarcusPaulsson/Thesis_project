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
        
    reachable = [False] * (n + 1)
    q = deque(main_courses)
    for course in main_courses:
        reachable[course] = True
    
    while q:
        u = q.popleft()
        for i in range(1, n + 1):
            if u in dependencies[i-1] and not reachable[i]:
                reachable[i] = True
                q.append(i)
                
    result = []
    
    for course in order:
        if reachable[course]:
            result.append(course)
            
    
    valid_result = []
    reachable_set = set()
    
    
    def check_dependencies(course, passed_courses):
        for dep in dependencies[course - 1]:
            if dep not in passed_courses:
                return False
        return True
    
    def find_path(current_path, courses_passed):
        if main_courses.issubset(courses_passed):
            return current_path
        
        
        
        next_courses = []
        for course in order:
            if course not in courses_passed and reachable[course] and check_dependencies(course, courses_passed):
                next_courses.append(course)
        
        
        
        
        best_path = None
        for course in next_courses:
            
            new_courses_passed = set(courses_passed)
            new_courses_passed.add(course)
            
            new_path = current_path + [course]
            
            
            path = find_path(new_path, new_courses_passed)
            if path:
                if best_path is None or len(path) < len(best_path):
                    best_path = path
        
        
        return best_path
        
    
    
    
    
    
    best_path = find_path([], set())
    
    if best_path is None:
        print("-1")
    else:
        print(len(best_path))
        print(*best_path)

solve()