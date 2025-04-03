def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    parents = {}
    
    def build_tree(arr):
        if not arr:
            return {}
        
        root = arr[0]
        children = []
        
        i = 1
        while i < len(arr):
            level_start = i
            j = i
            while j < len(arr) and arr[j] > arr[i-1]:
                j += 1
            
            children.append(arr[i:j])
            i = j
        
        tree = {}
        tree[root] = []
        
        for child_level in children:
            for child in child_level:
                tree[root].append(child)
                parents[child] = root
                
        for child_level in children:
            build_tree(child_level)
        
        return tree
    
    build_tree(a)
    
    max_depth = 0
    for i in range(1, n + 1):
        depth = 0
        curr = i
        while curr != 1:
          if curr not in parents:
            depth = -1
            break;
          curr = parents[curr]
          depth += 1
        if depth != -1:
            max_depth = max(max_depth, depth)
    
    print(max_depth)

t = int(input())
for _ in range(t):
    solve()