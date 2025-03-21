def find_cake_permutations(t, test_cases):
    results = []
    
    for case in test_cases:
        n, pieces = case
        degree = [0] * (n + 1)
        edges = {}

        # Count degrees and store edges
        for i, (a, b, c) in enumerate(pieces):
            degree[a] += 1
            degree[b] += 1
            degree[c] += 1
            edges[i + 1] = (a, b, c)

        # Find the starting vertex which has degree 2
        start_vertex = next(i for i in range(1, n + 1) if degree[i] == 2)

        # Reconstruct the order of vertices
        order = []
        visited_edges = set()
        current_vertex = start_vertex

        while len(order) < n:
            order.append(current_vertex)
            next_vertex = None
            
            for i in range(1, len(pieces) + 1):
                if i in visited_edges:
                    continue
                a, b, c = edges[i]
                if current_vertex in (a, b, c):
                    next_vertex = a if a != current_vertex else (b if b != current_vertex else c)
                    visited_edges.add(i)
                    break
            
            current_vertex = next_vertex

        # Create the permutation of vertices
        p = order

        # Create the order of cuts
        q = []
        for i in range(1, len(pieces) + 1):
            a, b, c = edges[i]
            if (a in p and b in p and c in p):
                idx = p.index(a)
                if p[(idx + 1) % n] == b and p[(idx + 2) % n] == c:
                    q.append(i)
        
        results.append((p, q))
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
idx = 1
for _ in range(t):
    n = int(data[idx])
    pieces = [tuple(map(int, data[idx + i + 1].split())) for i in range(n - 2)]
    test_cases.append((n, pieces))
    idx += n - 1

# Getting results
results = find_cake_permutations(t, test_cases)

# Printing output
output = []
for p, q in results:
    output.append(" ".join(map(str, p)))
    output.append(" ".join(map(str, q)))
print("\n".join(output))