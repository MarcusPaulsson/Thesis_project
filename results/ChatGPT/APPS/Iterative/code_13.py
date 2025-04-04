from collections import deque, defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n, k = map(int, data[0].split())
    main_courses = set(map(int, data[1].split()))

    dependencies = defaultdict(list)
    indegree = [0] * (n + 1)

    for i in range(1, n + 1):
        line = list(map(int, data[i + 1].split()))
        t_i = line[0]
        for dep in line[1:t_i + 1]:
            dependencies[dep].append(i)
            indegree[i] += 1

    # Topological sort to find the order of courses
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

    # Check if we can complete all main courses
    if not main_courses.issubset(set(order)):
        print(-1)
        return

    # Determine the minimum courses to take
    taken_courses = set()
    result = []

    for course in order:
        if course in main_courses or any(dep not in taken_courses for dep in dependencies[course]):
            result.append(course)
            taken_courses.add(course)

    print(len(result))
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()