from collections import deque, defaultdict

def find_course_order(n, k, main_courses, dependencies):
    # Create an adjacency list for dependencies and a list for in-degrees
    adj_list = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    # Build the graph
    for i in range(1, n + 1):
        dep = dependencies[i - 1]
        for dep_course in dep:
            adj_list[dep_course].append(i)
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
        
        # Reduce in-degree for dependent courses
        for next_course in adj_list[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    # Check if all main courses can be taken
    required_courses = set(main_courses)
    all_courses = set(order)

    if not required_courses.issubset(all_courses):
        return -1
    
    # Include all necessary courses
    result = []
    for course in order:
        if course in required_courses or any(dep in courses_taken for dep in dependencies[course - 1]):
            result.append(course)
    
    return len(result), result

# Input reading
n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
dependencies = []

for _ in range(n):
    dep_info = list(map(int, input().split()))
    dependencies.append(dep_info[1:])  # Only take the dependencies, ignore the first number

# Get the result
result = find_course_order(n, k, main_courses, dependencies)

# Print the result
if result == -1:
    print(-1)
else:
    m, course_order = result
    print(m)
    print(' '.join(map(str, course_order)))