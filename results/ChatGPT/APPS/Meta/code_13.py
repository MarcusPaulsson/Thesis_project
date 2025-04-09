from collections import deque, defaultdict

def find_courses(n, k, main_courses, dependencies):
    # Create a graph and a degree count
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    # Populate the graph and in-degree
    for course in range(1, n + 1):
        dep = dependencies[course - 1]
        for prereq in dep:
            graph[prereq].append(course)
            in_degree[course] += 1
            
    # Queue for courses that can be taken (in_degree == 0)
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    # List to keep track of the courses taken
    order = []
    taken_courses = set()
    
    # Process the courses
    while queue:
        current = queue.popleft()
        order.append(current)
        # If current is a main course, mark it as taken
        if current in main_courses:
            taken_courses.add(current)
        
        # Update the in-degree of the dependent courses
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all main courses are taken
    if len(taken_courses) < len(main_courses):
        return -1
    
    # Result is the total number of courses taken
    return len(order), order

# Input handling
n, k = map(int, input().split())
main_courses = set(map(int, input().split()))
dependencies = [list(map(int, input().split()[1:])) for _ in range(n)]

# Get the result
result = find_courses(n, k, main_courses, dependencies)

# Output the result
if result == -1:
    print(-1)
else:
    m, order = result
    print(m)
    print(' '.join(map(str, order)))