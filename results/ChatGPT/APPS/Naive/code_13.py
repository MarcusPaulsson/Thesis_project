from collections import deque, defaultdict

def find_courses(n, k, main_courses, dependencies):
    # Create a graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    # Build the graph and in-degree array
    for i in range(1, n + 1):
        for dep in dependencies[i - 1]:
            graph[dep].append(i)
            in_degree[i] += 1
    
    # Queue for courses with no dependencies
    queue = deque()
    for course in range(1, n + 1):
        if in_degree[course] == 0:
            queue.append(course)
    
    # To track the courses we need to take
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
    
    # Check if we can take all main courses
    if not all(course in courses_taken for course in main_courses):
        return -1
    
    # Collect the necessary courses to take
    necessary_courses = set(main_courses)
    for course in main_courses:
        # Traverse dependencies to find all necessary courses
        stack = [course]
        while stack:
            current = stack.pop()
            for dep in dependencies[current - 1]:
                if dep not in necessary_courses:
                    necessary_courses.add(dep)
                    stack.append(dep)
    
    # Filter the order to only include necessary courses
    final_order = [course for course in order if course in necessary_courses]
    
    return len(final_order), final_order

# Input reading
n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
dependencies = [list(map(int, input().split()[1:])) for _ in range(n)]

# Find the courses
result = find_courses(n, k, main_courses, dependencies)

# Output the result
if result == -1:
    print(-1)
else:
    m, course_order = result
    print(m)
    print(' '.join(map(str, course_order)))