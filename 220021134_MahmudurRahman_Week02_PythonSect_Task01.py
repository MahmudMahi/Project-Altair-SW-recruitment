import heapq
#start of dijkrista's algo
def path(n, edges, start, end):
    graph = {i: [] for i in range(1, n+1)}
    # creates a dict with node as key and a edges as value,
    # for example,
    #1:[]
    #2:[]
    for start, dest, val in edges:
        graph[start].append((val, dest))
        graph[dest].append((val, start))
    heap = [(0, start, [])]  # (cost, current_node, path)
    visited = set()
    while heap:
        cost, node, path = heapq.heappop(heap) #update for tthe small cost or min cost
        
        if node in visited:
            continue  
        path = path + [node]  
        visited.add(node)  
        if node == end:
            return path  
        for next_cost, next_node in graph[node]:
            if next_node not in visited:
                heapq.heappush(heap, (cost + next_cost, next_node, path))  

    return -1  #if no path exist

#start of main func
n = int(input())
e= int(input())
edges=[]
for i in range(0, e):
    s, d, v = map(int, data[i].split())
    edges.append((s, d, v))
start = 1
end = 5
path = dijkstra_shortest_path(n, edges, start, end)
print(shortest_path)
