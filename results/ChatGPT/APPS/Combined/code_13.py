from collections import deque, defaultdict

def find_course_order(n, k, main_courses, dependencies):
    indegree = [0] * (n + 1)
    graph = defaultdict(list)
    
    # Build the graph and indegree array
    for i in range(1, n + 1):
        for dep in dependencies[i - 1]:
            graph[dep].append(i)
            indegree[i] += 1
    
    # Queue for courses that can be taken (indegree 0)
    queue = deque(course for course in range(1, n + 1) if indegree[course] == 0)
    
    order = []
    taken_courses = set()
    
    # Process the courses
    while queue:
        course = queue.popleft()
        order.append(course)
        taken_courses.add(course)
        
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    # Check if all main courses can be taken
    if not all(main in taken_courses for main in main_courses):
        return -1
    
    # Collect the necessary courses
    necessary_courses = set(main_courses)
    final_order = []
    
    for course in order:
        if course in necessary_courses:
            necessary_courses.remove(course)
        final_order.append(course)
        if not necessary_courses:
            break
    
    return len(final_order), final_order

# Input reading
n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
dependencies = [list(map(int, input().split()[1:])) for _ in range(n)]

# Get the result
result = find_course_order(n, k, main_courses, dependencies)

# Output the result
if result == -1:
    print(-1)
else:
    print(result[0])
    print(' '.join(map(str, result[1])))