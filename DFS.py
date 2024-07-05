N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

# create graph
for _ in range(M):

    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) #both directions yeah?


def dfs(x):

    stack = [x]
    visited[x] = True
    count = 0
    while stack:
        y = stack.pop()
        for neighbor in graph[y]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                count+= 1
    return count

visited = [False for _ in range(N+1)]

print(dfs(1))
