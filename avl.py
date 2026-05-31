# AVL Tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(n):
    return n.height if n else 0

def balance(n):
    return height(n.left) - height(n.right) if n else 0

def right_rotate(y):
    x = y.left
    y.left = x.right
    x.right = y

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x

def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

def insert(root, key):
    if not root:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(height(root.left), height(root.right))

    bf = balance(root)

    if bf > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if bf < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

data = [30, 10, 20]
root = None

for x in data:
    root = insert(root, x)

print("Inorder AVL:")
inorder(root)


catatan :
# AVL Tree
# AVL Tree merupakan pengembangan dari Binary Search Tree (BST)
# yang menjaga keseimbangan tinggi pohon secara otomatis.
# Jika terjadi ketidakseimbangan, dilakukan rotasi kiri atau
# rotasi kanan untuk menyeimbangkan kembali tree.
# Program ini mengimplementasikan operasi insert dan traversal inorder.

class Node:
    ...
