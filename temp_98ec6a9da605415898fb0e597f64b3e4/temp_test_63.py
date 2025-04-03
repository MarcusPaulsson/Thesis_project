from collections import deque, defaultdict
import sys

input = sys.stdin.read
data = input().splitlines()

n, k = map(int, data[0].split())
main_courses = list(map(int, data[1].split()))

# Course dependencies
dependencies = defaultdict(list)
indegree = [0] * (n + 1)

# Read course dependencies
for i in range(1, n + 1):
    line = list(map(int, data[i + 1].split()))
    t_i = line[0]
    for j in range(1, t_i + 1):
        dependencies[line[j]].append(i)
        indegree[i] += 1

# To find the minimum courses to take, we need to ensure all main courses are covered
courses_to_take = set(main_courses)
visited = set()
queue = deque()

# Add main courses with no dependencies to the queue
for course in main_courses:
    if indegree[course] == 0:
        queue.append(course)

# BFS/Topological sort
result = []
while queue:
    current = queue.popleft()
    if current in visited:
        continue
    
    visited.add(current)
    result.append(current)

    for dependent in dependencies[current]:
        indegree[dependent] -= 1
        if indegree[dependent] == 0:
            queue.append(dependent)

# Check if we have visited all main courses
if not all(course in visited for course in main_courses):
    print(-1)
else:
    # We need to include all courses that provided prerequisites for main courses
    all_courses = set(result)
    for course in result:
        for dependent in dependencies[course]:
            all_courses.add(dependent)
    
    # Output the results
    print(len(all_courses))
    print(' '.join(map(str, sorted(all_courses))))