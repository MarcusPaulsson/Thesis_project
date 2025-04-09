from collections import defaultdict, deque
import sys

def find_course_order(n, k, main_courses, dependencies):
    graph = defaultdict(list)
    indegree = [0] * (n + 1)

    # Build the graph and calculate indegrees
    for course in range(1, n + 1):
        for dep in dependencies[course - 1]:
            graph[dep].append(course)
            indegree[course] += 1

    # Initialize queue with courses that have no prerequisites
    queue = deque(course for course in range(1, n + 1) if indegree[course] == 0)
    
    course_order = []
    
    while queue:
        current = queue.popleft()
        course_order.append(current)
        
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Check if all main courses can be completed
    required_courses = set(main_courses)
    taken_courses = set(course_order)

    if not required_courses.issubset(taken_courses):
        return -1

    # Gather the courses that need to be taken
    result_order = []
    for course in course_order:
        if course in required_courses or any(dep in taken_courses for dep in dependencies[course - 1]):
            result_order.append(course)

    return len(result_order), result_order

# Read input
input = sys.stdin.read
data = input().splitlines()
n, k = map(int, data[0].split())
main_courses = list(map(int, data[1].split()))
dependencies = [list(map(int, line.split()[1:])) for line in data[2:2 + n]]

# Get the result
result = find_course_order(n, k, main_courses, dependencies)

# Output the result
if result == -1:
    print(-1)
else:
    m, order = result
    print(m)
    print(' '.join(map(str, order)))