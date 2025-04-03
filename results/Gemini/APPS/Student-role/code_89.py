def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    parents = {}
    children = {}
    for i in range(1, n + 1):
        children[i] = []
    
    q = [a[0]]
    idx = 1
    
    while q:
        curr = q.pop(0)
        
        next_level = []
        while idx < n:
            if any(a[idx] in children[x] for x in a[:idx]):
                break
            children[curr].append(a[idx])
            parents[a[idx]] = curr
            next_level.append(a[idx])
            idx += 1
        
        q.extend(next_level)
        
    def get_height(root):
        max_depth = 0
        q = [(root, 0)]
        
        while q:
            node, depth = q.pop(0)
            max_depth = max(max_depth, depth)
            
            for child in children[node]:
                q.append((child, depth + 1))
                
        return max_depth
    
    print(get_height(1))

t = int(input())
for _ in range(t):
    solve()