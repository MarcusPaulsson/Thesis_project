from collections import deque, defaultdict

def main():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    
    dependencies = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        t_i = line[0]
        for dep in line[1:t_i + 1]:
            dependencies[dep].append(i)
            indegree[i] += 1
    
    # Queue for courses that can be taken (no dependencies)
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    
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
    
    # Check if all main courses can be taken
    if not all(course in taken_courses for course in main_courses):
        print(-1)
        return
    
    # Collect all courses needed to take
    result = []
    for course in main_courses:
        result.append(course)
        for dep in dependencies[course]:
            if dep not in result:
                result.append(dep)
    
    # Remove duplicates and sort by order of appearance
    result = list(dict.fromkeys(result))
    
    print(len(result))
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()