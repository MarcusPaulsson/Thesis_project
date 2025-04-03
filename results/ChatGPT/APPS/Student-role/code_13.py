from collections import deque, defaultdict

def find_course_order(n, k, main_courses, dependencies):
    # Create a graph for courses and track in-degrees
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    # Fill the graph and in-degree based on dependencies
    for i in range(1, n + 1):
        t_i, *deps = dependencies[i - 1]
        in_degree[i] = t_i
        for dep in deps:
            graph[dep].append(i)

    # Queue for courses that can be taken (in-degree == 0)
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    # List of courses to take
    order = []
    taken_courses = set()
    
    while queue:
        course = queue.popleft()
        order.append(course)
        taken_courses.add(course)
        
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if we can take all main courses
    if not all(course in taken_courses for course in main_courses):
        return -1

    # Return the result
    return len(order), order

# Input reading
n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
dependencies = [list(map(int, input().split())) for _ in range(n)]

# Finding the course order
result = find_course_order(n, k, main_courses, dependencies)

# Output result
if result == -1:
    print(-1)
else:
    m, order = result
    print(m)
    print(' '.join(map(str, order)))