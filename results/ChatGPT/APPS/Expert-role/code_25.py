def find_cake_and_order(t, test_cases):
    results = []
    
    for case in test_cases:
        n, pieces = case
        edges = {}
        piece_indices = []
        
        for index, (a, b, c) in enumerate(pieces):
            piece_indices.append(index + 1)
            for u, v in [(a, b), (b, c), (c, a)]:
                if u not in edges:
                    edges[u] = set()
                edges[u].add(v)

        # Find the order of vertices
        start_vertex = next(iter(edges))
        order = []
        visited = set()
        current_vertex = start_vertex
        
        while len(order) < n:
            order.append(current_vertex)
            visited.add(current_vertex)
            next_vertex = None
            
            for neighbor in edges[current_vertex]:
                if neighbor not in visited:
                    next_vertex = neighbor
                    break
            
            if next_vertex is None:
                break
            
            current_vertex = next_vertex
        
        # Construct the order of cutting pieces
        cut_order = []
        for index, (a, b, c) in enumerate(pieces):
            if a in order and b in order and c in order:
                cut_order.append(index + 1)

        results.append((order, cut_order))
    
    output = []
    for order, cut_order in results:
        output.append(" ".join(map(str, order)))
        output.append(" ".join(map(str, cut_order)))
    
    return output


# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

line_index = 1
for _ in range(t):
    n = int(data[line_index])
    pieces = []
    for i in range(n - 2):
        pieces.append(tuple(map(int, data[line_index + 1 + i].split())))
    test_cases.append((n, pieces))
    line_index += n - 1 + 1

# Get results
results = find_cake_and_order(t, test_cases)

# Print results
for line in results:
    print(line)