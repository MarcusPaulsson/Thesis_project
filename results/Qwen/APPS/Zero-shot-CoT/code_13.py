from collections import defaultdict, deque

def main():
    n, k = map(int, input().split())
    main_courses = set(map(int, input().split()))
    
    dependencies = defaultdict(list)
    for i in range(1, n + 1):
        t_i = int(input())
        dependencies[i] = list(map(int, input().split()))
    
    # Topological sort
    in_degree = [0] * (n + 1)
    for i in range(1, n + 1):
        for dep in dependencies[i]:
            in_degree[dep] += 1
    
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    order = []
    visited = set()
    
    while queue:
        course = queue.popleft()
        order.append(course)
        visited.add(course)
        
        for dep in dependencies[course]:
            in_degree[dep] -= 1
            if in_degree[dep] == 0:
                queue.append(dep)
    
    # Check if all main courses are visited
    if len(visited.intersection(main_courses)) == k:
        print(len(order))
        print(*order)
    else:
        print(-1)

if __name__ == "__main__":
    main()