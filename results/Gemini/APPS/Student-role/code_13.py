from collections import defaultdict, deque

def solve():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    dependencies = []
    for _ in range(n):
        dependencies.append(list(map(int, input().split()))[1:])

    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    for i in range(n):
        for dep in dependencies[i]:
            graph[dep].append(i + 1)
            in_degree[i + 1] += 1

    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    result = []
    count = 0
    while q:
        node = q.popleft()
        result.append(node)
        count += 1

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    if count != n:
        print("-1")
        return

    required_courses = set(main_courses)
    visited = [False] * (n + 1)
    path = []

    def dfs(course):
        if visited[course]:
            return
        visited[course] = True
        for dep in dependencies[course-1]:
            if not visited[dep]:
                dfs(dep)
                
        path.append(course)

    for course in main_courses:
        if not visited[course]:
            dfs(course)

    path.reverse()
    
    final_path = []
    final_set = set()
    
    for course in path:
        if course not in final_set:
            final_path.append(course)
            final_set.add(course)
    
    
    main_courses_present = True
    for course in main_courses:
        if course not in final_set:
            main_courses_present = False
            break
            
    if not main_courses_present:
        print("-1")
        return

    print(len(final_path))
    print(*final_path)

solve()