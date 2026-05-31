# Graph - Adjacency List

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

print("Adjacency List:")

for node in graph:
    print(node, "->", graph[node])

catatan :
# Graph (Adjacency List)
# Graph adalah struktur data yang terdiri dari vertex (simpul)
# dan edge (hubungan antar simpul).
# Program ini menggunakan representasi Adjacency List untuk
# menyimpan hubungan antar node dan menampilkannya ke layar.

graph = {
    ...
}
