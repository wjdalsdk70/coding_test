import heapq

V, E = map(int, input().split())
arr = [[] for _ in range(V+1)]
visit = [False for _ in range(V+1)]  # Use boolean for clarity

# Input all edges
for _ in range(E):
    a, b, edge_cost = map(int, input().split())
    arr[a].append((edge_cost, b))  # Store as tuple for easier heap operations
    arr[b].append((edge_cost, a))

# Prim's algorithm
total_cost = 0  # Use a different variable for total cost
heap = [(0, 1)]  # Start from node 1 with 0 cost
cnt = 0

while heap and cnt < V:
    c, node = heapq.heappop(heap)
    if not visit[node]:  # Only process unvisited nodes
        visit[node] = True
        total_cost += c
        cnt += 1
        for edge_cost, neighbor in arr[node]:
            if not visit[neighbor]:
                heapq.heappush(heap, (edge_cost, neighbor))

if cnt == V:
    print(total_cost)
else:
    print("MST cannot be formed, some nodes are not reachable")
