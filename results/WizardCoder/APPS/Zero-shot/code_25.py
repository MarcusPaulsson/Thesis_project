from itertools import permutations

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        vertices = []
        
        for i in range(n - 2):
            vertex1, vertex2, vertex3 = map(int, input().split())
            vertices.append((vertex1, vertex2, vertex3))
            
        for p in permutations([i + 1 for i in range(n)]):
            result_p = list(p)
            result_q = []
            remaining_vertices = set()
            
            for triangle in vertices:
                if len(set(triangle)) == 3 and all(vertex in p for vertex in triangle):
                    for vertex in triangle:
                        result_p.remove(vertex)
                    
                    remaining_vertices.add(triangle[0])
                    remaining_vertices.add(triangle[1])
                    remaining_vertices.add(triangle[2])
            
            if len(remaining_vertices) == 3:
                for i, vertex in enumerate(result_p):
                    if vertex not in remaining_vertices and (i + 1) % n != 0:
                        result_q.append(vertex)
            
            if len(result_q) == n - 2:
                print(' '.join(map(str, result_p)) + '\n' + ' '.join(map(str, result_q)))
                break

if __name__ == "__main__":
    main()