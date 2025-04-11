from collections import deque, defaultdict

def main():
    n, k = map(int, input().split())
    main_courses = set(map(int, input().split()))
    
    # Build the graph and indegree count
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        t_i = data[0]
        dependencies = data[1:t_i + 1]
        for dep in dependencies:
            graph[dep].append(i)
            indegree[i] += 1
    
    # Topological sort using Kahn's algorithm
    queue = deque()
    for course in range(1, n + 1):
        if indegree[course] == 0:
            queue.append(course)
    
    order = []
    while queue:
        current = queue.popleft()
        order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if we can complete all main courses
    completed_courses = set()
    for course in order:
        if course in main_courses:
            completed_courses.add(course)
        if len(completed_courses) == len(main_courses):
            break
    
    if len(completed_courses) < len(main_courses):
        print(-1)
        return
    
    # Collect all courses needed to complete the main courses
    needed_courses = set()
    for course in main_courses:
        stack = [course]
        while stack:
            current = stack.pop()
            if current not in needed_courses:
                needed_courses.add(current)
                stack.extend(graph[current])
    
    # Filter the order to only include needed courses
    result = [course for course in order if course in needed_courses]
    
    print(len(result))
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()