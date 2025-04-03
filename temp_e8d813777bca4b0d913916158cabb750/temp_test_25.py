def solve():
    n = int(input())
    triangles = []
    for _ in range(n - 2):
        triangles.append(list(map(int, input().split())))

    def is_adjacent(arr, a, b):
        for i in range(len(arr) - 1):
            if (arr[i] == a and arr[i+1] == b) or (arr[i] == b and arr[i+1] == a):
                return True
        if (arr[0] == a and arr[-1] == b) or (arr[0] == b and arr[-1] == a):
            return True
        return False

    def check_triangle(polygon, triangle):
        a, b, c = triangle
        
        a_idx = -1
        b_idx = -1
        c_idx = -1
        for i in range(len(polygon)):
            if polygon[i] == a:
                a_idx = i
            elif polygon[i] == b:
                b_idx = i
            elif polygon[i] == c:
                c_idx = i
        
        if a_idx == -1 or b_idx == -1 or c_idx == -1:
            return False
        
        
        if (a_idx + 1) % len(polygon) == b_idx and (a_idx - 1 + len(polygon)) % len(polygon) == c_idx:
            return True
        if (a_idx + 1) % len(polygon) == c_idx and (a_idx - 1 + len(polygon)) % len(polygon) == b_idx:
            return True
        
        return False

    import itertools
    for perm in itertools.permutations(range(1, n + 1)):
        
        p = list(perm)
        
        
        cutting_order = []
        remaining_polygon = p[:]
        
        triangle_indices = list(range(n - 2))
        
        
        
        def find_cutting_order(polygon, available_triangles):
            if not available_triangles:
                return True
            
            for i in available_triangles:
                triangle = triangles[i]
                if check_triangle(polygon, triangle):
                    cutting_order.append(i + 1)
                    
                    a,b,c = triangle
                    
                    a_idx = polygon.index(a)
                    b_idx = polygon.index(b)
                    c_idx = polygon.index(c)
                    
                    if (a_idx + 1) % len(polygon) == b_idx and (a_idx - 1 + len(polygon)) % len(polygon) == c_idx:
                        
                        new_polygon = polygon[:]
                        new_polygon.pop(a_idx)
                        
                    elif (a_idx + 1) % len(polygon) == c_idx and (a_idx - 1 + len(polygon)) % len(polygon) == b_idx:
                        new_polygon = polygon[:]
                        new_polygon.pop(a_idx)
                    else:
                        return False
                        
                    remaining_triangles = available_triangles[:]
                    remaining_triangles.remove(i)

                    if find_cutting_order(new_polygon, remaining_triangles):
                        return True
                    else:
                        cutting_order.pop()
            return False
        
        if find_cutting_order(remaining_polygon, triangle_indices):
            print(*p)
            print(*cutting_order)
            return

t = int(input())
for _ in range(t):
    solve()