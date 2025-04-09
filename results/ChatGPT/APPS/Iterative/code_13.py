from collections import deque, defaultdict

def main():
    n, k = map(int, input().split())
    main_courses = set(map(int, input().split()))
    
    dependencies = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        t_i = line[0]
        for j in range(1, t_i + 1):
            dep_course = line[j]
            dependencies[dep_course].append(i)
            indegree[i] += 1
    
    queue = deque()
    
    for course in range(1, n + 1):
        if indegree[course] == 0:
            queue.append(course)
    
    order = []
    taken_courses = set()
    
    while queue:
        course = queue.popleft()
        order.append(course)
        taken_courses.add(course)
        
        for next_course in dependencies[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    if not main_courses.issubset(taken_courses):
        print(-1)
        return
    
    result = []
    for course in order:
        if course in main_courses or any(dep in taken_courses for dep in dependencies[course]):
            result.append(course)
    
    print(len(result))
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()