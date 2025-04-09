from collections import deque, defaultdict

def topological_sort(n, dependencies):
    indegree = [0] * (n + 1)
    graph = defaultdict(list)
    
    for course, deps in dependencies.items():
        for dep in deps:
            graph[dep].append(course)
            indegree[course] += 1
    
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    order = []
    while queue:
        course = queue.popleft()
        order.append(course)
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return order

def find_courses(n, k, main_courses, dependencies):
    order = topological_sort(n, dependencies)
    if len(order) < n:
        return -1  # cycle detected or not all courses can be taken
    
    course_set = set(main_courses)
    to_take = []
    taken_courses = set()
    
    for course in order:
        if course in course_set or any(dep in taken_courses for dep in dependencies[course]):
            to_take.append(course)
            taken_courses.add(course)
            if course in course_set:
                course_set.remove(course)
    
    if course_set:
        return -1  # not all main courses can be taken
    
    return len(to_take), to_take

# Input reading
n, k = map(int, input().split())
main_courses = list(map(int, input().split()))
dependencies = {}

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    dependencies[i] = data[1:]  # skip the first number which is the count of dependencies

result = find_courses(n, k, main_courses, dependencies)

if result == -1:
    print(-1)
else:
    m, courses = result
    print(m)
    print(' '.join(map(str, courses)))