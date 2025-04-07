from collections import deque, defaultdict

def main():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    
    # Adjacency list for the graph of courses
    dependencies = defaultdict(list)
    # In-degree count for topological sorting
    in_degree = [0] * (n + 1)
    
    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        t_i = data[0]
        for dep in data[1:t_i + 1]:
            dependencies[dep].append(i)
            in_degree[i] += 1

    # Queue for courses with no dependencies (in-degree of 0)
    queue = deque()
    
    # Start with all courses that have no dependencies
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    
    # List to maintain the order of completed courses
    order = []
    passed_courses = set()
    
    while queue:
        course = queue.popleft()
        order.append(course)
        passed_courses.add(course)
        
        for dependent_course in dependencies[course]:
            in_degree[dependent_course] -= 1
            if in_degree[dependent_course] == 0:
                queue.append(dependent_course)

    # Check if we can complete all main courses
    if not all(course in passed_courses for course in main_courses):
        print(-1)
        return

    # Collect all courses needed to pass
    needed_courses = set(main_courses)
    result_courses = []
    
    for course in order:
        result_courses.append(course)
        if course in needed_courses:
            needed_courses.remove(course)
        if not needed_courses:
            break
    
    # The result courses will be the ones passed until all main are completed
    print(len(result_courses))
    print(" ".join(map(str, result_courses)))

if __name__ == "__main__":
    main()