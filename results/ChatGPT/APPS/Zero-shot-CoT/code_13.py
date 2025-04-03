from collections import defaultdict, deque
import sys

input = sys.stdin.read
data = input().splitlines()

n, k = map(int, data[0].split())
main_courses = list(map(int, data[1].split()))

# Create an adjacency list and in-degree counter for each course
dependencies = defaultdict(list)
in_degree = [0] * (n + 1)

# Read course dependencies
for i in range(1, n + 1):
    line = list(map(int, data[i + 1].split()))
    t_i = line[0]
    for j in range(1, t_i + 1):
        dependencies[line[j]].append(i)
        in_degree[i] += 1

# To track which courses we need to take
to_take = set(main_courses)
# To track all courses we need to take
all_courses = set(main_courses)

# Use a queue to perform topological sorting
queue = deque()
for course in range(1, n + 1):
    if in_degree[course] == 0:
        queue.append(course)

order_of_courses = []

while queue:
    course = queue.popleft()
    order_of_courses.append(course)

    # If this course is a main course, add its dependencies to the set
    if course in to_take:
        all_courses.add(course)
        for dependent in dependencies[course]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

# If we couldn't take all main courses, return -1
if all_courses != set(main_courses):
    print(-1)
else:
    # Print the result
    print(len(order_of_courses))
    print(" ".join(map(str, order_of_courses)))