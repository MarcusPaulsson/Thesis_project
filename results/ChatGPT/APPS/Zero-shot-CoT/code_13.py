from collections import deque, defaultdict

def main():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        t_i = data[0]
        dependencies = data[1:t_i + 1]
        for dep in dependencies:
            graph[dep].append(i)
            in_degree[i] += 1

    to_pass = set(main_courses)
    queue = deque()
    passed = set()
    order = []

    for course in range(1, n + 1):
        if in_degree[course] == 0:
            queue.append(course)

    while queue:
        course = queue.popleft()
        order.append(course)
        passed.add(course)

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if not to_pass.issubset(passed):
        print(-1)
        return

    result = []
    for course in order:
        if course in to_pass:
            result.append(course)
            to_pass.remove(course)

    print(len(order))
    print(" ".join(map(str, order)))

if __name__ == "__main__":
    main()