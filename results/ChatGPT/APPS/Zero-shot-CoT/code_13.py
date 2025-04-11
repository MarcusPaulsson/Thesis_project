from collections import deque, defaultdict

def main():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    
    dependencies = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        t_i = data[0]
        for j in range(1, t_i + 1):
            dep_course = data[j]
            dependencies[dep_course].append(i)
            indegree[i] += 1
    
    queue = deque()
    for course in range(1, n + 1):
        if indegree[course] == 0:
            queue.append(course)
    
    order = []
    passed_courses = set()
    
    while queue:
        current = queue.popleft()
        order.append(current)
        passed_courses.add(current)
        
        for dependent in dependencies[current]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                queue.append(dependent)
    
    if not all(indegree[course] == 0 for course in main_courses):
        print(-1)
        return
    
    result = []
    for course in order:
        if course in main_courses or any(dep in passed_courses for dep in dependencies[course]):
            result.append(course)
    
    print(len(result))
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()