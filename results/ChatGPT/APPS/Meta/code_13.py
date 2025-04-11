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
    
    # Queue for courses that can be taken (in-degree of 0)
    queue = deque()
    for course in range(1, n + 1):
        if in_degree[course] == 0:
            queue.append(course)
    
    # To track the courses we need to take
    taken_courses = []
    main_courses_set = set(main_courses)
    courses_to_take = set(main_courses)
    
    # Process the courses
    while queue:
        course = queue.popleft()
        taken_courses.append(course)
        
        # If this course is a main course, remove it from the set of courses to take
        if course in courses_to_take:
            courses_to_take.remove(course)
        
        # Process the dependent courses
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if we have taken all main courses
    if courses_to_take:
        return -1
    
    # Return the result
    return len(taken_courses), taken_courses

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
    m, courses = result
    print(m)
    print(' '.join(map(str, courses)))