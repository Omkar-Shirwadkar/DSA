class BinaryTreeNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def inord(root):
    arr = []
    inorder(root, arr)
    return arr
def inorder(root, arr):
    if root:
        inorder(root.left, arr)
        arr.append(root.data)
        inorder(root.right, arr)

def preord(root):
    arr = []
    preorder(root, arr)
    return arr
def preorder(root, brr):
    if root:
        brr.append(root.data)
        preorder(root.left, brr)
        preorder(root.right, brr)

def postord(root):
    arr = []
    postorder(root, arr)
    return arr
def postorder(root, crr):
    if root:
        postorder(root.left, crr)
        postorder(root.right, crr)
        crr.append(root.data)

def levelOrder(root):
    if not root:
        return []
    ans = []
    queue = []
    queue.append(root)
    while queue:
        size = len(queue)
        level = []
        for i in range(size):
            ele = queue[0]
            queue.pop(0)
            if ele.left:
                queue.append(ele.left)
            if ele.right:
                queue.append(ele.right)
            level.append(ele.data)
        ans.append(level)
    return ans

if __name__ == "__main__":
    ele = BinaryTreeNode(1)
    ele.left = BinaryTreeNode(2)
    ele.right = BinaryTreeNode(3)
    ele.left.left = BinaryTreeNode(4)
    ele.left.right = BinaryTreeNode(5)
    ele.right.left = BinaryTreeNode(6)
    ele.right.right = BinaryTreeNode(7)
    print("Inorder Traversal: ", inord(ele))
    print("Preorder Traversal: ", preord(ele))
    print("Postorder Traversal: ", postord(ele))
    print("Level Order Traversal: ", levelOrder(ele))