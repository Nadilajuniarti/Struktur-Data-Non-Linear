# Depth First Search (DFS)

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

print("Hasil DFS:")
dfs(graph, "A")

catatan :
# Depth First Search (DFS)
# DFS adalah algoritma penelusuran graph yang menelusuri
# satu cabang sedalam mungkin sebelum berpindah ke cabang lain.
# Program ini menggunakan rekursi untuk melakukan traversal
# graph mulai dari node A.

graph = {
    ...
}
