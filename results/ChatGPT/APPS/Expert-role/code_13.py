from collections import defaultdict, deque
import sys

input = sys.stdin.read
data = input().splitlines()

n, k = map(int, data[0].split())
main_courses = list(map(int, data[1].split()))

# Dependency graph and in-degree count
dependencies = defaultdict(list)
in_degree = [0] * (n + 1)

# Read course dependencies
for i in range(2, n + 2):
    line = list(map(int, data[i].split()))
    t_i = line[0]
    for j in range(1, t_i + 1):
        dependencies[line[j]].append(i - 1)  # course i-2 depends on line[j]
        in_degree[i - 1] += 1  # Increase in-degree for course i-2

# Topological sorting using Kahn's algorithm
queue = deque()
order = []
passed_courses = set()

# Start with courses with no dependencies
for i in range(1, n + 1):
    if in_degree[i - 1] == 0:
        queue.append(i)

while queue:
    course = queue.popleft()
    order.append(course)
    passed_courses.add(course)

    # Reduce in-degree of dependent courses
    for dependent in dependencies[course]:
        in_degree[dependent] -= 1
        if in_degree[dependent] == 0:
            queue.append(dependent + 1)

# Check if all main courses can be passed
if not all(course in passed_courses for course in main_courses):
    print(-1)
else:
    # We need to ensure we pass the main courses in the order needed
    result = []
    for course in order:
        if course in main_courses:
            result.append(course)
            main_courses.remove(course)
        if not main_courses:
            break

    # Include other passed courses if required
    for course in order:
        if course not in result and len(result) < len(passed_courses):
            result.append(course)

    print(len(result))
    print(" ".join(map(str, result)))