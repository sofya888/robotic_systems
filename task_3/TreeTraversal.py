
from collections import deque
from BinaryTreeNode import BinaryTree
class TreeTraversal:
    @staticmethod
    def inorder(node):
        res = []
        if node:
            res += TreeTraversal.inorder(node.left)
            res.append(node.value)
            res += TreeTraversal.inorder(node.right)
        return res

    @staticmethod
    def preorder(node):
        res = []
        if node:
            res.append(node.value)
            res += TreeTraversal.preorder(node.left)
            res += TreeTraversal.preorder(node.right)
        return res

    @staticmethod
    def postorder(node):
        res = []
        if node:
            res += TreeTraversal.postorder(node.left)
            res += TreeTraversal.postorder(node.right)
            res.append(node.value)
        return res

    @staticmethod
    def level_order(node):
        if not node:
            return []
        res, q = [], deque([node])
        while q:
            cur = q.popleft()
            res.append(cur.value)
            if cur.left:  q.append(cur.left)
            if cur.right: q.append(cur.right)
        return res

# Собираем дерево как BST вручную
tree = BinaryTree(50)
tree.insert_left(tree.root, 30)
tree.insert_right(tree.root, 70)
tree.insert_left(tree.root.left, 20)
tree.insert_right(tree.root.left, 40)
tree.insert_left(tree.root.right, 60)
tree.insert_right(tree.root.right, 80)

print("Inorder:", TreeTraversal.inorder(tree.root))
print("Preorder:", TreeTraversal.preorder(tree.root))
print("Postorder:", TreeTraversal.postorder(tree.root))
print("Level:", TreeTraversal.level_order(tree.root))