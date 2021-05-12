class Node:
    def __init__(self, dataval):
        self.val = dataval
        self.left = None
        self.right = None
        self.parent = None

class BTree:
    '''
    Binary Search tree: All nodes follow this property - all left descendants <= n < all right descendants.
    '''
    def __init__(self, dataval):
        n = Node(dataval)
        self.root = n
    