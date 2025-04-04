import sys
import threading

def main():
    import sys
    import threading

    def dfs(node, parent, depth, adj_list, depths, parents):
        depths[node] = depth
        parents[node] = parent
        for neighbor in adj_list[node]:
            if neighbor != parent:
                dfs(neighbor, node, depth + 1, adj_list, depths, parents)

    def find_lca(u, v, parents, depths):
        if depths[u] < depths[v]:
            u, v = v, u
        while depths[u] > depths[v]:
            u = parents[u]
        while u != v:
            u = parents[u]
            v = parents[v]
        return u

    def max_edges_in_paths(n, edges):
        adj_list = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        depths = [0] * (n + 1)
        parents = [0] * (n + 1)
        dfs(1, 0, 0, adj_list, depths, parents)
        max_edges = 0
        best_a, best_b, best_c = 0, 0, 0
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                lca_ab = find_lca(a, b, parents, depths)
                for c in range(b + 1, n + 1):
                    lca_ac = find_lca(a, c, parents, depths)
                    lca_bc = find_lca(b, c, parents, depths)
                    edges_in_paths = depths[a] + depths[b] + depths[c] - 2 * depths[lca_ab] - 2 * depths[lca_ac] - 2 * depths[lca_bc] + depths[find_lca(lca_ab, lca_ac, parents, depths)]
                    if edges_in_paths > max_edges:
                        max_edges = edges_in_paths
                        best_a, best_b, best_c = a, b, c
        return max_edges, best_a, best_b, best_c

    n = int(sys.stdin.readline())
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n - 1)]
    max_edges, a, b, c = max_edges_in_paths(n, edges)
    print(max_edges)
    print(a, b, c)

threading.Thread(target=main).start()