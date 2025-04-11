from collections import deque, defaultdict

def find_course_order(n, k, main_courses, dependencies):
    # Build the graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for dep in dependencies[i - 1]:
            graph[dep].append(i)
            in_degree[i] += 1
    
    # Queue for courses that can be taken (in-degree 0)
    queue = deque()
    for course in range(1, n + 1):
        if in_degree[course] == 0:
            queue.append(course)
    
    order = []
    courses_taken = set()
    
    while queue:
        course = queue.popleft()
        order.append(course)
        courses_taken.add(course)
        
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    # Check if all main courses can be taken
    if not all(course in courses_taken for course in main_courses):
        return -1
    
    # Collect all courses needed to take
    needed_courses = set(main_courses)
    for course in main_courses:
        needed_courses.update(get_dependencies(course, graph, courses_taken))
    
    # Filter the order to only include needed courses
    final_order = [course for course in order if course in needed_courses]
    
    return len(final_order), final_order

def get_dependencies(course, graph, courses_taken):
    dependencies = set()
    queue = deque([course])
    
    while queue:
        current = queue.popleft()
        for next_course in graph[current]:
            if next_course not in courses_taken:
                dependencies.add(next_course)
                queue.append(next_course)
    
    return dependencies

# Input reading
n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
dependencies = [list(map(int, input().split()[1:])) for _ in range(n)]

# Find the course order
result = find_course_order(n, k, main_courses, dependencies)

# Output the result
if result == -1:
    print(-1)
else:
    m, order = result
    print(m)
    print(' '.join(map(str, order)))