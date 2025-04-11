from collections import deque, defaultdict
import sys

input = sys.stdin.read
data = input().splitlines()

n, k = map(int, data[0].split())
main_courses = list(map(int, data[1].split()))
dependencies = defaultdict(list)
in_degree = [0] * (n + 1)

# Read dependencies
for i in range(1, n + 1):
    line = list(map(int, data[i + 1].split()))
    t_i = line[0]
    for dep in line[1:t_i + 1]:
        dependencies[dep].append(i)
        in_degree[i] += 1

# Topological sorting using Kahn's algorithm
queue = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

order = []
passed_courses = set()

while queue:
    course = queue.popleft()
    order.append(course)
    passed_courses.add(course)
    for next_course in dependencies[course]:
        in_degree[next_course] -= 1
        if in_degree[next_course] == 0:
            queue.append(next_course)

# Check if all main courses can be passed
if not all(course in passed_courses for course in main_courses):
    print(-1)
else:
    # Collect all courses that need to be passed
    result_courses = set()
    for course in main_courses:
        result_courses.add(course)
        for dep in dependencies[course]:
            result_courses.add(dep)

    # Ensure we have a valid order
    result_courses = list(dict.fromkeys(order))  # Remove duplicates while preserving order
    result_courses = [course for course in result_courses if course in passed_courses]

    print(len(result_courses))
    print(' '.join(map(str, result_courses)))