from collections import deque, defaultdict

def find_course_order(n, k, main_courses, dependencies):
    # Create an adjacency list and an in-degree counter
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    # Build the graph and in-degree array
    for course_id in range(1, n + 1):
        for dep in dependencies[course_id - 1]:
            graph[dep].append(course_id)
            in_degree[course_id] += 1

    # Queue for courses with no dependencies
    queue = deque(course_id for course_id in range(1, n + 1) if in_degree[course_id] == 0)

    passed_courses = []
    main_courses_set = set(main_courses)
    main_courses_passed = set()
    
    while queue:
        current_course = queue.popleft()
        passed_courses.append(current_course)
        
        # If the current course is a main course, mark it as passed
        if current_course in main_courses_set:
            main_courses_passed.add(current_course)
        
        # Process all courses dependent on the current course
        for neighbor in graph[current_course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if all main courses are passed
    if main_courses_passed != main_courses_set:
        return -1
    
    return len(passed_courses), passed_courses

# Input reading
n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
dependencies = [list(map(int, input().split()))[1:] for _ in range(n)]

# Get the result
result = find_course_order(n, k, main_courses, dependencies)

# Output
if result == -1:
    print(-1)
else:
    m, order = result
    print(m)
    print(" ".join(map(str, order)))