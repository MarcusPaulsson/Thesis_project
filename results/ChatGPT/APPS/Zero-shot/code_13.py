from collections import deque, defaultdict
import sys

input = sys.stdin.read
data = input().splitlines()

n, k = map(int, data[0].split())
main_courses = list(map(int, data[1].split()))
main_set = set(main_courses)

# Create the dependency graph and a reverse dependency count
dependencies = defaultdict(list)
in_degree = [0] * (n + 1)

# Read the course dependencies
for i in range(2, 2 + n):
    course_info = list(map(int, data[i].split()))
    t_i = course_info[0]
    for j in range(1, t_i + 1):
        dep_course = course_info[j]
        dependencies[dep_course].append(i - 1)  # i - 2 + 2 = i - 1 (0-indexed)
        in_degree[i - 1] += 1

# Topological sort using Kahn's algorithm
queue = deque()
for i in range(n):
    if in_degree[i] == 0:
        queue.append(i)

order = []
while queue:
    current = queue.popleft()
    order.append(current + 1)  # Store 1-indexed course number
    for neighbor in dependencies[current + 1]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

# Set of passed courses
passed_courses = set(order)

# Check if all main courses can be completed
if not main_set.issubset(passed_courses):
    print(-1)
else:
    # Collect the minimum courses needed to complete all main courses
    result = []
    for course in order:
        if course in main_set or any(dep in passed_courses for dep in dependencies[course]):
            result.append(course)

    print(len(result))
    print(' '.join(map(str, result)))