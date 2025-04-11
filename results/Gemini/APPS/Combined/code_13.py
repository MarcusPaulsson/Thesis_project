from collections import deque

def solve():
    n, k = map(int, input().split())
    main_courses = set(map(int, input().split()))
    dependencies = []
    for _ in range(n):
        line = list(map(int, input().split()))
        dependencies.append(line[1:])

    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for i in range(n):
        for dependency in dependencies[i]:
            graph[dependency].append(i + 1)
            in_degree[i + 1] += 1

    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    required_courses = set(main_courses)
    
    reachable = [False] * (n + 1)
    
    q = deque(main_courses)
    for course in main_courses:
        reachable[course] = True
    
    while q:
        u = q.popleft()
        for i in range(1, n + 1):
            for dep in dependencies[i-1]:
                if dep == u and not reachable[i]:
                    reachable[i] = True
                    q.append(i)
                    required_courses.add(i)

    
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for i in range(n):
        for dependency in dependencies[i]:
            if (i+1) in required_courses and dependency in required_courses:
                graph[dependency].append(i + 1)
                in_degree[i + 1] += 1
    
    queue = deque()
    for i in required_courses:
        if in_degree[i] == 0:
            queue.append(i)

    course_order = []
    visited_count = 0

    while queue:
        course = queue.popleft()
        course_order.append(course)
        visited_count += 1

        for dependent_course in graph[course]:
            in_degree[dependent_course] -= 1
            if in_degree[dependent_course] == 0:
                queue.append(dependent_course)

    if visited_count != len(required_courses):
        print("-1")
        return

    print(len(course_order))
    print(*course_order)

solve()