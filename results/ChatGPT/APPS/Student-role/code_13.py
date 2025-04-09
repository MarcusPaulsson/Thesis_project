from collections import deque, defaultdict

def topological_sort(n, prerequisites):
    in_degree = [0] * (n + 1)
    graph = defaultdict(list)
    
    for course, deps in enumerate(prerequisites, start=1):
        for dep in deps:
            graph[dep].append(course)
            in_degree[course] += 1

    # Queue for the courses with no prerequisites
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    order = []
    while queue:
        course = queue.popleft()
        order.append(course)
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == n else []

def minimum_courses_to_pass(n, k, main_courses, prerequisites):
    order = topological_sort(n, prerequisites)
    
    if not order:
        return -1

    passed = set()
    result = []

    for course in order:
        if course in main_courses or any(dep in passed for dep in prerequisites[course - 1]):
            if course not in passed:
                result.append(course)
                passed.add(course)

    if all(main in passed for main in main_courses):
        return len(result), result
    else:
        return -1

# Read input
n, k = map(int, input().split())
main_courses = set(map(int, input().split()))
prerequisites = [list(map(int, input().split()[1:])) for _ in range(n)]

# Get result
result = minimum_courses_to_pass(n, k, main_courses, prerequisites)

# Print output
if result == -1:
    print(-1)
else:
    m, courses = result
    print(m)
    print(' '.join(map(str, courses)))