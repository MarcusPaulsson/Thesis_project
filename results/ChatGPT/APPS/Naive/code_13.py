from collections import defaultdict, deque
import sys

def topological_sort(n, dependencies):
    in_degree = [0] * (n + 1)
    graph = defaultdict(list)

    # Build the graph and in-degree count
    for course, deps in dependencies.items():
        for dep in deps:
            graph[dep].append(course)
            in_degree[course] += 1

    # Queue for courses with no prerequisites
    zero_in_degree = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            zero_in_degree.append(i)

    order = []
    while zero_in_degree:
        course = zero_in_degree.popleft()
        order.append(course)
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                zero_in_degree.append(next_course)

    return order

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    n, k = map(int, data[0].split())
    main_courses = list(map(int, data[1].split()))
    
    dependencies = defaultdict(list)
    for i in range(n):
        line = list(map(int, data[i + 2].split()))
        t_i = line[0]
        dependencies[i + 1] = line[1:t_i + 1]

    # Get the topological order of courses
    order = topological_sort(n, dependencies)

    # Set for fast lookup of main courses
    main_set = set(main_courses)
    passed_courses = set()
    result_order = []

    # Process courses in topological order
    for course in order:
        if course in main_set or any(dep in passed_courses for dep in dependencies[course]):
            result_order.append(course)
            passed_courses.add(course)

    if not main_set.issubset(passed_courses):
        print(-1)
    else:
        print(len(result_order))
        print(" ".join(map(str, result_order)))

if __name__ == "__main__":
    main()