from collections import defaultdict, deque
import sys

input = sys.stdin.read
data = input().splitlines()

n, k = map(int, data[0].split())
main_courses = list(map(int, data[1].split()))
dependencies = defaultdict(list)
in_degree = [0] * (n + 1)

# Read dependencies
for i in range(1, n + 1):
    course_info = list(map(int, data[i + 1].split()))
    t_i = course_info[0]
    for dep in course_info[1:t_i + 1]:
        dependencies[dep].append(i)
        in_degree[i] += 1

# Topological sort using Kahn's algorithm
queue = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

order = []
courses_to_pass = set(main_courses)

while queue:
    course = queue.popleft()
    order.append(course)
    
    for dependent in dependencies[course]:
        in_degree[dependent] -= 1
        if in_degree[dependent] == 0:
            queue.append(dependent)

# Check if we can pass all main courses
passed_courses = set()
result_order = []

for course in order:
    if course in courses_to_pass:
        passed_courses.add(course)
        result_order.append(course)
        courses_to_pass.remove(course)
    
    # If we have passed all main courses, we can finish
    if not courses_to_pass:
        break

if courses_to_pass:
    print(-1)
else:
    # We need to include all courses that are required to pass main courses
    # Collect all the courses that have been used to get to the main courses
    final_passed_courses = set()
    for course in result_order:
        if course in passed_courses or course in main_courses:
            final_passed_courses.add(course)
            for dep in dependencies[course]:
                if dep not in final_passed_courses:
                    final_passed_courses.add(dep)
    
    final_passed_courses = sorted(final_passed_courses)
    print(len(final_passed_courses))
    print(" ".join(map(str, final_passed_courses)))