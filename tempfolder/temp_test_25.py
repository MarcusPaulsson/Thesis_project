def solve():
    import sys
    from collections import defaultdict

    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        
        triangles = []
        adjacency = defaultdict(int)
        
        for i in range(n - 2):
            a, b, c = map(int, data[index].split())
            triangles.append((a, b, c))
            adjacency[a] += 1
            adjacency[b] += 1
            adjacency[c] += 1
            index += 1
        
        # Find the vertex that appears the most
        max_vertex = max(adjacency, key=adjacency.get)
        
        # Now we find the order of vertices
        p = []
        used = set()
        current = max_vertex
        
        # Start the order with the max vertex
        p.append(current)
        used.add(current)
        
        # Next we need to find neighbors in the triangles
        for _ in range(n - 1):
            for a, b, c in triangles:
                if current in (a, b, c):
                    for neighbor in (a, b, c):
                        if neighbor != current and neighbor not in used:
                            p.append(neighbor)
                            used.add(neighbor)
                            current = neighbor
                            break
                    else:
                        continue
                    break
        
        # The order of cutting
        q = []
        for i in range(n - 2):
            q.append(i + 1)
        
        results.append(' '.join(map(str, p)))
        results.append(' '.join(map(str, q)))
    
    print('\n'.join(results))

# Call solve() when the script runs
if __name__ == "__main__":
    solve()