class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# build tree
a = TreeNode(8)
a.left = TreeNode(7)
a.left.left = TreeNode(3)
a.left.right = TreeNode(6)
a.right = TreeNode(9)
a.right.left = TreeNode(10)
a.right.right = TreeNode(12)

'''
    8
 7     9
3 6  10 12 
'''

pre_order, in_order, post_order = [], [], []


def dfs(node):
    if not node: return
    pre_order.append(node.val) 
    dfs(node.left)
    in_order.append(node.val)
    dfs(node.right)
    post_order.append(node.val)
dfs(a)

print("pre-order:" , pre_order, "in-order:", in_order, "post-order:", post_order)
