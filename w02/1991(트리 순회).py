class Node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def pre(node):
    print(node.value, end='')
    if node.left != ".":
        pre(tree[node.left])
    if node.right != ".":
        pre(tree[node.right])
        
def mid(node):
    if node.left != ".":
        mid(tree[node.left])
    print(node.value, end='')
    if node.right != ".":
        mid(tree[node.right])

def post(node):
    if node.left != ".":
        post(tree[node.left])
    if node.right != ".":
        post(tree[node.right])
    print(node.value, end='')

n = int(input())
inputs = [input().split() for _ in range(n)]
tree = {}
for value, left, right in inputs:
    tree[value] = Node(value, left, right)
    
pre(tree['A'])
print()
mid(tree['A'])
print()
post(tree['A'])