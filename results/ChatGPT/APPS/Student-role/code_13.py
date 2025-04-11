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
    queue = deque()
    for course in range(1, n + 1):
        if indegree[course] == 0:
            queue.append(course)
    
    order = []
    taken_courses = set()
    
    while queue:
        course = queue.popleft()
        order.append(course)
        taken_courses.add(course)
        
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    # Check if all main courses can be taken
    for main_course in main_courses:
        if main_course not in taken_courses:
            return -1
    
    # Collect the minimum courses needed to take
    result = []
    for course in order:
        if course in main_courses or any(dep in taken_courses for dep in dependencies[course - 1]):
            result.append(course)
    
    return len(result), result

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