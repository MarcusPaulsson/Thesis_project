def find_cake_and_cut_order(t, test_cases):
    results = []
    for case in test_cases:
        n, pieces = case
        from collections import defaultdict

        # Step 1: Create a graph representation of the pieces
        graph = defaultdict(set)
        piece_index = {}
        
        for index, (a, b, c) in enumerate(pieces):
            graph[a].add(b)
            graph[a].add(c)
            graph[b].add(a)
            graph[b].add(c)
            graph[c].add(a)
            graph[c].add(b)
            piece_index[(a, b, c)] = index + 1  # Store the 1-based index
            
        # Step 2: Find a starting triangle
        start_triangle = pieces[0]
        unique_vertices = set(start_triangle)
        order = list(start_triangle)
        cut_order = []

        # Step 3: Process the triangle cutting
        used = set()
        used.add(tuple(start_triangle))
        
        while len(order) < n:
            a, b, c = order[-3], order[-2], order[-1]
            cut_order.append(piece_index[(a, b, c)])

            # Find the next vertex
            next_vertex = None
            for vertex in graph[c]:
                if vertex not in unique_vertices:
                    next_vertex = vertex
                    break
            
            if next_vertex is not None:
                unique_vertices.add(next_vertex)
                order.append(next_vertex)
                # Update the graph to remove the current triangle
                graph[a].remove(b)
                graph[a].remove(c)
                graph[b].remove(a)
                graph[b].remove(c)
                graph[c].remove(a)
                graph[c].remove(b)
                # Remove the triangle from used
                used.add((a, b, c))
                used.add((b, c, a))
                used.add((c, a, b))
            
        # Step 4: Prepare the output
        results.append((order, cut_order))
    
    # Print results
    output = []
    for order, cut_order in results:
        output.append(" ".join(map(str, order)))
        output.append(" ".join(map(str, cut_order)))
    
    return output

# Input handling
import sys
input = sys.stdin.read
data = input().splitlines()
t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n = int(data[index])
    pieces = []
    for j in range(n - 2):
        piece = tuple(map(int, data[index + j + 1].split()))
        pieces.append(piece)
    test_cases.append((n, pieces))
    index += n - 1 + 1

# Get the results
results = find_cake_and_cut_order(t, test_cases)

# Print the results
print("\n".join(results))