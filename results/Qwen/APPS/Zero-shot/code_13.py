from collections import defaultdict, deque

def main():
    n, k = map(int, input().split())
    main_courses = set(map(int, input().split()))
    dependencies = defaultdict(list)
    for i in range(1, n+1):
        t, *deps = map(int, input().split())
        dependencies[i] = deps

    # Topological sort
    in_degree = [0] * (n+1)
    for i in range(1, n+1):
        for dep in dependencies[i]:
            in_degree[dep] += 1

    queue = deque([i for i in range(1, n+1) if in_degree[i] == 0])
    order = []
    while queue:
        course = queue.popleft()
        order.append(course)
        for dep in dependencies[course]:
            in_degree[dep] -= 1
            if in_degree[dep] == 0:
                queue.append(dep)

    # Check if all main courses are in the order
    if len(order) < n or not main_courses.issubset(set(order)):
        print(-1)
    else:
        print(len(order))
        print(*order)

if __name__ == "__main__":
    main()