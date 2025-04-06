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
        for dependency in dependencies[i]:
            adj[dependency].append(i + 1)
            in_degree[i + 1] += 1
            
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
            
    order = []
    passed = set()
    
    while q:
        u = q.popleft()
        order.append(u)
        passed.add(u)
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
                
    if len(passed) != n:
        print("-1")
        return

    necessary = set(main_courses)
    result = []
    
    def dfs(course):
        if course in result:
            return
        
        
        for dependency in dependencies[course-1]:
            if dependency not in result:
                dfs(dependency)
        result.append(course)
        
    for course in main_courses:
        if course not in result:
            dfs(course)
            
    result_set = set(result)
    
    
    
    for i in range(1,n+1):
        if i in result_set:
            continue
        
        is_needed = False
        for main_course in main_courses:
            if main_course == i:
                is_needed = True
                break
            
            to_check = deque([main_course])
            visited = set()
            
            while to_check:
                curr = to_check.popleft()
                if curr == i:
                    is_needed = True
                    break
                
                if curr in visited:
                    continue
                visited.add(curr)
                
                for dependency in dependencies[curr-1]:
                    to_check.append(dependency)
            if is_needed:
                break
        if is_needed:
            dfs(i)
    
    
    
    print(len(result))
    print(*result)
    

solve()