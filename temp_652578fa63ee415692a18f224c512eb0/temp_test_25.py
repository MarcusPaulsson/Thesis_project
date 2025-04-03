def solve():
    n = int(input())
    triangles = []
    for _ in range(n - 2):
        triangles.append(list(map(int, input().split())))

    def check_permutation(permutation, triangles_permutation):
        for start_dir in [1, -1]:
            for start_idx in range(n):
                p = []
                for i in range(n):
                    p.append(permutation[(start_idx + i * start_dir) % n])

                remaining_vertices = set(p)
                
                for triangle_idx in triangles_permutation:
                    triangle = triangles[triangle_idx - 1]
                    
                    indices = []
                    for v in triangle:
                        try:
                            indices.append(p.index(v))
                        except ValueError:
                            break
                    else:
                        indices.sort()
                        
                        if len(indices) != 3:
                            break

                        
                        
                        
                        
                        
                        
                        if (indices[1] - indices[0] == 1 and indices[2] - indices[1] == 1) or \
                           (indices[0] == 0 and indices[1] == n-1 and indices[2] == n-2) or \
                           (indices[0] == 0 and indices[1] == 1 and indices[2] == n-1) or \
                           (indices[1] - indices[0] == 1 and indices[2] == n-1 and indices[0] == 0) or\
                           (indices[1] - indices[0] == 1 and indices[2] == n-1 and indices[1] == n-2):
                            
                            
                            
                            new_p = []
                            for i in range(len(p)):
                                if i not in indices:
                                    new_p.append(p[i])
                            p = new_p

                            for v in triangle:
                                if v in remaining_vertices:
                                    remaining_vertices.remove(v)
                                    
                            if n - len(p) >= n - 2:
                                return p, triangles_permutation
                            
                        
                        
                        
                        
                        
                        elif (indices[0] == 0 and indices[1] == (n-1) and indices[2] == (n-2)) or (indices[0] == 0 and indices[1] == 1 and indices[2] == (n-1)):
                            new_p = []
                            for i in range(len(p)):
                                if i not in indices:
                                    new_p.append(p[i])
                            p = new_p

                            for v in triangle:
                                if v in remaining_vertices:
                                    remaining_vertices.remove(v)
                                    
                            if n - len(p) >= n - 2:
                                return p, triangles_permutation

                            
                        
                        
                        
                        

        return None, None

    import itertools
    
    for permutation in itertools.permutations(range(1, n + 1)):
        for triangles_permutation in itertools.permutations(range(1, n - 1)):
            p, q = check_permutation(list(permutation), list(triangles_permutation))

            if p is not None:
                
                
                
                
                
                permutation_result = []
                
                for start_dir in [1, -1]:
                    for start_idx in range(n):
                        p_temp = []
                        for i in range(n):
                            p_temp.append(permutation[(start_idx + i * start_dir) % n])
                        
                        
                        permutation_result = p_temp
                        
                        print(*permutation_result)
                        print(*q)
                        
                        return
                
    
    

t = int(input())
for _ in range(t):
    solve()