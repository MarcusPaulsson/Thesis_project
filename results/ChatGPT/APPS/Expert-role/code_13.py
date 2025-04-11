from collections import deque, defaultdict

def find_course_order(n, k, main_courses, dependencies):
    indegree = [0] * (n + 1)
    graph = defaultdict(list)
    
    for i in range(1, n + 1):
        for dep in dependencies[i - 1]:
            graph[dep].append(i)
            indegree[i] += 1
    
    queue = deque()
    for course in range(1, n + 1):
        if indegree[course] == 0:
            queue.append(course)
    
    order = []
    passed_courses = set()
    
    while queue:
        course = queue.popleft()
        order.append(course)
        passed_courses.add(course)
        
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    if not all(course in passed_courses for course in main_courses):
        return -1
    
    return len(order), order

# Input reading
n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
dependencies = [list(map(int, input().split()[1:])) for _ in range(n)]

# Finding the course order
result = find_course_order(n, k, main_courses, dependencies)

# Output
if result == -1:
    print(-1)
else:
    print(result[0])
    print(' '.join(map(str, result[1])))