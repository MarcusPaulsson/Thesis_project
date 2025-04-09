from collections import defaultdict, deque

def solve():
    n, k = map(int, input().split())
    main_courses = set(map(int, input().split()))
    dependencies = []
    for _ in range(n):
        line = list(map(int, input().split()))
        dependencies.append(line[1:])
    
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for i in range(n):
        for dependency in dependencies[i]:
            graph[dependency].append(i + 1)
            in_degree[i + 1] += 1
            
    def find_required_courses(main_courses, dependencies):
        required_courses = set(main_courses)
        added = True
        while added:
            added = False
            for i in range(1, n + 1):
                if i in required_courses:
                    for dependency in dependencies[i-1]:
                        if dependency not in required_courses:
                            required_courses.add(dependency)
                            added = True
        return required_courses
    
    required_courses = find_required_courses(main_courses, dependencies)
    
    q = deque()
    in_degree = [0] * (n + 1)
    adj = defaultdict(list)
    
    for i in range(n):
        for dependency in dependencies[i]:
            adj[dependency].append(i + 1)
    
    for i in range(1, n + 1):
        for neighbor in adj[i]:
            if i in required_courses and neighbor in required_courses:
                in_degree[neighbor] += 1
    
    for i in range(1, n + 1):
        if i in required_courses and in_degree[i] == 0:
            q.append(i)
    
    result = []
    while q:
        u = q.popleft()
        result.append(u)
        for v in adj[u]:
            if u in required_courses and v in required_courses:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
                    
    if len(result) != len(required_courses):
        print("-1")
        return
    
    print(len(result))
    print(*result)
    
solve()