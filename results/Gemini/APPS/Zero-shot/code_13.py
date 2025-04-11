from collections import deque

def solve():
    n, k = map(int, input().split())
    main_courses = list(map(int, input().split()))
    dependencies = []
    for _ in range(n):
        dependencies.append(list(map(int, input().split()))[1:])

    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for dep in dependencies[i-1]:
            graph[dep].append(i)
            indegree[i] += 1

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0 :
            q.append(i)
            
    result = []
    count = 0
    
    while q:
        u = q.popleft()
        result.append(u)
        count+=1

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if count != n:
        print("-1")
        return
    
    necessary = set(main_courses)
    
    
    
    
    visited = [False] * (n+1)
    ans=[]
    
    def dfs(node):
        if visited[node]:
            return
        visited[node] = True
        
        for neighbor in dependencies[node-1]:
            dfs(neighbor)
            
        ans.append(node)
    
    for course in main_courses:
        dfs(course)
        
    ans = ans[::-1]
    
    
    
    print(len(ans))
    print(*ans)

solve()