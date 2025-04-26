from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    # graph.append(list(map(int, input().split())))
    # 1 2 1 -> 2
    # 1 3 1 -> 3
    # 2 3 2 -> 3
    # 2 4 2 -> 4
    # [[], [1, 2], [1, 3], [2, 3], [2, 4]]
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)

distance = [-1] * (n + 1)
distance[x] = 0

queue = deque([x])
while queue:
    now = queue.popleft()

    for nxt in graph[now]: # now에서 이동 가능한 곳
        if distance[nxt] == -1:
            distance[nxt] = distance[now] + 1
            queue.append(nxt)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
