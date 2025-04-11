from collections import deque, defaultdict

def find_course_order(n, k, main_courses, dependencies):
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    # Build the graph and in-degree array
    for course in range(1, n + 1):
        for dep in dependencies[course - 1]:
            graph[dep].append(course)
            in_degree[course] += 1
    
    queue = deque()
    
    # Add all courses that have no dependencies
    for course in range(1, n + 1):
        if in_degree[course] == 0:
            queue.append(course)
    
    order = []
    courses_to_take = set(main_courses)
    
    while queue:
        current = queue.popleft()
        order.append(current)
        
        if current in courses_to_take:
            courses_to_take.remove(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if courses_to_take:
        return -1
    
    return len(order), order

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