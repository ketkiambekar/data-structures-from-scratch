#****************
#  IN PROGRESS
#***************
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

    def insert(self, val):
        '''
        Inserts a node in a binary tree

        Args:
            val: Value of the Node
            
        Returns:
            Nothing
        '''
        #Traverse to the location of adding the node:
        while self.right==None or self.left ==None.

    def delete(self, val):
        '''
        Deletes a node in a binary tree

        Args:
            val: Value of the Node. (If there are two nodes with same value, the first occurence will be deleted.)
        
        Returns:
            Nothing
        '''
        pass

    def rebalance_tree(self, val):
        '''
        Checks the nodes for 

        Args:
            val: Value of the Node
        
        Returns:
            Nothing
        '''
        pass

    def preorder_traversal(self):
        '''
        Prints nodes in the order: current, left child, right child.
        '''
        pass
    def inorder_traversal(self):
        '''
        Prints nodes in the order: left child, current, right child.
        '''
        pass
    def postorder_traversal(self):
        '''
        Prints nodes in the order: left child, current, right child.
        '''
        pass
    def print_nicely(self):
        '''
        Prints the trees in a tree pattern, with spaces and all. 
        '''
        pass

