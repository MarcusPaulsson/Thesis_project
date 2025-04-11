from collections import deque, defaultdict
import sys

input = sys.stdin.read
data = input().splitlines()

n, k = map(int, data[0].split())
main_courses = list(map(int, data[1].split()))
dependencies = defaultdict(list)
indegree = [0] * (n + 1)

# Read dependencies
for i in range(1, n + 1):
    line = list(map(int, data[i + 1].split()))
    t_i = line[0]
    for dep in line[1:t_i + 1]:
        dependencies[dep].append(i)
        indegree[i] += 1

# Topological sort using Kahn's algorithm
queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

order = []
while queue:
    course = queue.popleft()
    order.append(course)
    for next_course in dependencies[course]:
        indegree[next_course] -= 1
        if indegree[next_course] == 0:
            queue.append(next_course)

# Check if all courses can be completed
if len(order) < n:
    print(-1)
    sys.exit()

# Determine the courses to take
taken_courses = set()
result = []

def dfs(course):
    if course in taken_courses:
        return
    taken_courses.add(course)
    for dep in dependencies[course]:
        dfs(dep)
    result.append(course)

for main_course in main_courses:
    dfs(main_course)

# Add any additional courses needed
for course in order:
    if course not in taken_courses:
        dfs(course)

print(len(result))
print(' '.join(map(str, result[::-1])))