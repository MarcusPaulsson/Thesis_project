from collections import deque, defaultdict

def main():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    
    # Adjust for 0-based indexing
    main_courses = [x - 1 for x in main_courses]
    
    dependencies = defaultdict(list)
    in_degree = [0] * n
    
    for i in range(n):
        data = list(map(int, input().split()))
        t_i = data[0]
        for dep in data[1:t_i + 1]:
            dependencies[dep - 1].append(i)
            in_degree[i] += 1
    
    # Queue for courses that can be taken (in-degree 0)
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    order = []
    taken_courses = set()
    
    while queue:
        course = queue.popleft()
        order.append(course)
        taken_courses.add(course)
        
        for dependent in dependencies[course]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    # Check if we can take all main courses
    if not all(course in taken_courses for course in main_courses):
        print(-1)
        return
    
    # We need to pass all main courses and their dependencies
    result = []
    for course in order:
        result.append(course + 1)  # Adjust back to 1-based indexing
        if course in main_courses:
            main_courses.remove(course)
            if not main_courses:
                break
    
    # Add any remaining courses that are not main but are taken
    result = list(dict.fromkeys(result))  # Remove duplicates while preserving order
    print(len(result))
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()