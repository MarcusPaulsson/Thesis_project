from collections import deque, defaultdict

def find_courses(n, k, main_courses, dependencies):
    # Create a graph and a list to track in-degrees
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    # Build the graph and in-degree count
    for i in range(1, n + 1):
        for dep in dependencies[i - 1]:
            graph[dep].append(i)
            in_degree[i] += 1

    # Queue for courses that can be taken (in-degree 0)
    queue = deque()
    for course in range(1, n + 1):
        if in_degree[course] == 0:
            queue.append(course)

    # To track the courses to take
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

    # Collect all courses that need to be taken
    result = []
    for main in main_courses:
        result.append(main)
        for course in order:
            if course not in result and (course not in main_courses or course in taken_courses):
                result.append(course)

    return len(result), result

# Input reading
n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
dependencies = [list(map(int, input().split()[1:])) for _ in range(n)]

# Solve the problem
result = find_courses(n, k, main_courses, dependencies)

# Output the result
if result == -1:
    print(-1)
else:
    print(result[0])
    print(' '.join(map(str, result[1])))