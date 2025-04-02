from collections import defaultdict
import heapq

def dijkstra(adj_list):
    n = len(adj_list)
    dist = [float('inf')] * n
    dist[0] = 0
    visited = set()
    pq = [(0, 0)] # (distance, node)
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited: continue
        visited.add(u)
        for v, w in adj_list[u]:
            dist_through_u = d + w
            if dist_through_u < dist[v]:
                dist[v] = dist_through_u
                heapq.heappush(pq, (dist_through_u, v))
    return dist

def min_coins(n, m_and_p):
    graph = [[] for _ in range(n)]
    for i in range(n):
        m, p = m_and_p[i]
        if m == 0: # If the voter can be convinced without paying coins, add an edge to himself
            graph[i].append((i, 0))
        else:
            for j in range(m): # Otherwise, create edges to all other voters who can convince m people
                graph[i].append((j, p)
    return dijkstra(graph)[n-1]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        m_and_p = []
        for i in range(n):
            m, p = map(int, input().split())
            m_and_p.append((m, p)
        print(min_coins(n, m_and_p))