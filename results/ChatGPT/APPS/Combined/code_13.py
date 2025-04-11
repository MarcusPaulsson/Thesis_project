from collections import defaultdict, deque
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    n, k = map(int, data[0].split())
    main_courses = set(map(int, data[1].split()))
    
    dependencies = defaultdict(list)
    indegree = [0] * (n + 1)
    
    for i in range(2, n + 2):
        line = list(map(int, data[i].split()))
        t_i = line[0]
        for j in range(1, t_i + 1):
            dependencies[line[j]].append(i - 1)  # i - 2 + 2 = i
            indegree[i - 1] += 1
    
    # To track courses that need to be taken
    courses_to_take = set(main_courses)
    queue = deque(main_courses)
    
    while queue:
        current = queue.popleft()
        for prereq in dependencies[current]:
            indegree[prereq] -= 1
            if indegree[prereq] == 0:
                queue.append(prereq)
                courses_to_take.add(prereq)
    
    # Check if we can take all necessary courses
    if len(courses_to_take) < len(main_courses):
        print(-1)
        return
    
    # Topological sort to determine the order of courses
    order = []
    queue = deque(i for i in range(1, n + 1) if indegree[i] == 0 and i in courses_to_take)
    
    while queue:
        current = queue.popleft()
        order.append(current)
        for prereq in dependencies[current]:
            indegree[prereq] -= 1
            if indegree[prereq] == 0 and prereq in courses_to_take:
                queue.append(prereq)
    
    if len(order) < len(courses_to_take):
        print(-1)
    else:
        print(len(order))
        print(' '.join(map(str, order)))

if __name__ == "__main__":
    main()