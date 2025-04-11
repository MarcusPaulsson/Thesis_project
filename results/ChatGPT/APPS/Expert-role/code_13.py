from collections import deque, defaultdict
import sys

input = sys.stdin.read
data = input().splitlines()

n, k = map(int, data[0].split())
main_courses = list(map(int, data[1].split()))
dependencies = defaultdict(list)
in_degree = [0] * (n + 1)

# Read dependencies
for i in range(2, n + 2):
    line = list(map(int, data[i].split()))
    t_i = line[0]
    for dep in line[1:t_i + 1]:
        dependencies[dep].append(i - 1)  # i - 2 + 1 = i - 1 (0-indexed)
        in_degree[i - 1] += 1

# Topological sort using Kahn's algorithm
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

# Check if all main courses can be taken
needed_courses = set(main_courses)
for course in order:
    if course in needed_courses:
        needed_courses.remove(course)
    if not needed_courses:
        break

if needed_courses:
    print(-1)
else:
    print(len(order))
    print(" ".join(map(str, order)))