# Breadth First Search (BFS)

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

def bfs(graph, start):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in graph[node]:
                queue.append(neighbor)

print("Hasil BFS:")
bfs(graph, "A")

catatan :
# Breadth First Search (BFS)
# BFS adalah algoritma penelusuran graph yang bekerja per level.
# Algoritma ini menggunakan Queue untuk menyimpan node yang akan dikunjungi.
# Pada program ini, BFS digunakan untuk menelusuri graph
# mulai dari node A.

from collections import deque

graph = {
    ...
}
