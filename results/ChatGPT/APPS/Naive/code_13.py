from collections import deque, defaultdict

def main_courses_sequence(n, k, main_courses, dependencies):
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    # Build the graph and compute in-degrees
    for course_id in range(1, n + 1):
        for dep in dependencies[course_id - 1]:
            graph[dep].append(course_id)
            in_degree[course_id] += 1

    # Queue for courses that can be taken (in-degree of 0)
    queue = deque()
    for course_id in range(1, n + 1):
        if in_degree[course_id] == 0:
            queue.append(course_id)

    order = []
    taken_courses = set()

    # Process the courses in topological order
    while queue:
        course_id = queue.popleft()
        order.append(course_id)
        taken_courses.add(course_id)

        for neighbor in graph[course_id]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if we can take all main courses
    if not all(course in taken_courses for course in main_courses):
        return -1

    # Find all courses needed to take
    needed_courses = set(main_courses)
    for course in main_courses:
        stack = [course]
        while stack:
            curr = stack.pop()
            for dep in dependencies[curr - 1]:
                if dep not in needed_courses:
                    needed_courses.add(dep)
                    stack.append(dep)

    # Filter the courses to include only the needed ones
    result = [course for course in order if course in needed_courses]
    return len(result), result

# Input reading
n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
dependencies = []

for _ in range(n):
    line = list(map(int, input().split()))
    dependencies.append(line[1:])

# Get the result
result = main_courses_sequence(n, k, main_courses, dependencies)

# Output
if result == -1:
    print(-1)
else:
    m, course_order = result
    print(m)
    print(" ".join(map(str, course_order)))