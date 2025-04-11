from collections import deque, defaultdict

def find_course_order(n, k, main_courses, dependencies):
    # Create a graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    # Fill the graph and in-degree based on dependencies
    for i in range(1, n + 1):
        t_i, *deps = dependencies[i - 1]
        in_degree[i] = t_i
        for dep in deps:
            graph[dep].append(i)

    # Queue for courses that can be taken (in-degree 0)
    queue = deque()
    for course in range(1, n + 1):
        if in_degree[course] == 0:
            queue.append(course)

    order = []
    taken_courses = set()

    # Process the courses
    while queue:
        course = queue.popleft()
        order.append(course)
        taken_courses.add(course)

        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    # Check if all main courses can be taken
    for main in main_courses:
        if main not in taken_courses:
            return -1

    # Collect the minimum courses needed
    result_order = []
    for course in order:
        if course in main_courses or any(dep in taken_courses for dep in dependencies[course - 1][1:]):
            result_order.append(course)

    return len(result_order), result_order

# Input reading
n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
dependencies = [list(map(int, input().split())) for _ in range(n)]

# Finding the course order
result = find_course_order(n, k, main_courses, dependencies)

# Output the result
if result == -1:
    print(-1)
else:
    m, course_order = result
    print(m)
    print(' '.join(map(str, course_order)))