def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def calculate_height(parents):
        depth = {}
        depth[1] = 0
        for i in range(2, n + 1):
            depth[i] = -1

        for i in range(2, n + 1):
            curr = i
            d = 0
            while curr != 1:
                curr = parents[curr]
                d += 1
            depth[i] = d

        max_depth = 0
        for i in range(1, n + 1):
            max_depth = max(max_depth, depth[i])
        return max_depth

    def find_min_height():
        min_height = float('inf')
        
        def check_tree(parents):
            
            adj = [[] for _ in range(n + 1)]
            for i in range(2, n + 1):
                adj[parents[i]].append(i)
                
            for i in range(1, n + 1):
                adj[i].sort()
                
            bfs_order = []
            q = [1]
            visited = {1}
            
            while q:
                u = q.pop(0)
                bfs_order.append(u)
                
                for v in adj[u]:
                    if v not in visited:
                        q.append(v)
                        visited.add(v)
            
            bfs_order_check = [a[i] for i in range(n)]
           
            if bfs_order == bfs_order_check:
                return True
            else:
                return False

        def generate_trees():
            
            import itertools
            
            possible_parents = {}
            for i in range(2, n + 1):
                possible_parents[i] = []
                
            
            
            level_start_indices = [0]
            curr_level_start = 1
            
            while curr_level_start < n:
                
                next_level_start = curr_level_start + 1
                
                
                while next_level_start < n and len([x for x in possible_parents.keys() if x == a[next_level_start]]) == 0:
                   
                    next_level_start +=1
                
                level_start_indices.append(curr_level_start)
                curr_level_start = next_level_start
                
            
            
            level_start_indices.append(n)
            
            
            for i in range(1, n + 1):
                possible_parents[i] = []
                
            
            
            for i in range(1, len(level_start_indices)):
                
                start_index = level_start_indices[i - 1]
                end_index = level_start_indices[i]
                
                for j in range(start_index, end_index):
                    node = a[j]
                    
                    for k in range(level_start_indices[i - 1] -1 , level_start_indices[i-2] -1, -1):
                        possible_parents[node].append(a[k])
                
        
            
            
            
            possible_parent_lists = [possible_parents[i] for i in range(2, n + 1)]
            
            
            
            for parent_combination in itertools.product(*possible_parent_lists):
                
                parents = {}
                for i in range(2, n + 1):
                    parents[i] = parent_combination[i - 2]
                    
                if check_tree(parents):
                    height = calculate_height(parents)
                    nonlocal min_height
                    min_height = min(min_height, height)
            
        
        
        parents = {}
        for i in range(2, n + 1):
            parents[i] = 1
        
        
        
        
        
        
        
        level_start_indices = [0]
        curr_level_start = 1
        
        while curr_level_start < n:
            
            next_level_start = curr_level_start + 1
                
            while next_level_start < n and (a[next_level_start] not in [x for x in range(1,n+1)]):
                next_level_start +=1
            
            level_start_indices.append(curr_level_start)
            curr_level_start = next_level_start
            
        level_start_indices.append(n)
        
        
        
        
        
        parents = {}
        for i in range(2,n+1):
            parents[a[i]] = 1
        
        
        
        
        
        height_initial = calculate_height(parents)
        
        
        
        
        
        
        import itertools
        
        possible_parents = {}
        for i in range(2, n + 1):
            possible_parents[i] = []
                
            
            
        level_start_indices = [0]
        curr_level_start = 1
            
        while curr_level_start < n:
            
            next_level_start = curr_level_start + 1
                
            while next_level_start < n and (a[next_level_start] not in [x for x in range(1,n+1)]):
                next_level_start +=1
                
            level_start_indices.append(curr_level_start)
            curr_level_start = next_level_start
                
        
        level_start_indices.append(n)
            
            
            
        for i in range(1, n + 1):
            possible_parents[i] = []
                
            
            
        for i in range(1, len(level_start_indices)):
                
            start_index = level_start_indices[i - 1]
            end_index = level_start_indices[i]
                
            for j in range(start_index, end_index):
                node = a[j]
                    
                
                for k in range(level_start_indices[i - 1] - 1, level_start_indices[i-2] - 1, -1):
                    possible_parents[node].append(a[k])
                
            
        
            
        
        possible_parent_lists = [possible_parents[i] for i in range(2, n + 1)]
            
        
            
        for parent_combination in itertools.product(*possible_parent_lists):
                
            parents = {}
            for i in range(2, n + 1):
                parents[i] = parent_combination[i - 2]
                    
            if check_tree(parents):
                height = calculate_height(parents)
                
                min_height = min(min_height, height)
        
        
        return min_height

    print(find_min_height())


t = int(input())
for _ in range(t):
    solve()