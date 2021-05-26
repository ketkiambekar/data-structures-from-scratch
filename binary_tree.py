# A binary Search Tree Implementation
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

    def printTree(self):
        '''
        Prints the nodes of the tree in a pyramid format
        '''
        print("Printing Tree..." , end="\n")
        #Queue that contains all nodes
        q1 =[self.root, None]
        levels =0

        #Populate the queue to be printed later.
        i=0
        while i<len(q1):
            current = q1[i]
            if current == None:
                if q1[i] == None and q1[i-1]==None:
                    break
                q1.append(None)
                levels+=1
                i+=1
                continue

            if current.left:
                q1.append(current.left)
            if current.right:
                q1.append(current.right)
            
            i+=1
        
        #Print in a tree format
        print(" "*levels, end="  ")
        for n in q1:
            if n == None:
                print("\n", " "*levels, end="")
                levels-=1
            else:
                print( n.val, end="  ")
            
        
    def add(self, dataval):
        '''
        Inserts a node in a binary tree

        Args:
            val: Value of the Node
            
        Returns:
            Nothing
        '''
        pointer = self.root
        while True:
            if dataval >=pointer.val:
                if pointer.right: 
                    pointer = pointer.right
                else:
                    pointer.right = Node(dataval)
                    break
            else:
                if pointer.left:
                    pointer=pointer.left
                else:
                    pointer.left= Node(dataval)
                    break
                
        
    def PostOrderTraversal(self, n=None):
        '''
        Prints nodes in the order: left child, right child, root.
        Args:
            n: Root node of the tree (optional)
        '''
        
        #implement using recursion

        if n==None:
            n=self.root
     
        if n.left==None and n.right ==None:
            print(n.val, end= " ")
            return
        else:
            if n.left: self.PostOrderTraversal(n.left)
            if n.right: self.PostOrderTraversal(n.right)
            print (n.val, end=" ")
            

    
    def PreOrderTraversal(self, n=None):
        '''
        Prints nodes in the order: current, left child, right child.
        Args:
            n: Root node of the tree (optional)
        '''
        
        #implement using recursion
        if n==None:
            n=self.root
     
        if n.left==None and n.right ==None:
            print(n.val, end= " ")
            return
        else:
            print (n.val, end=" ")
            if n.left: self.PreOrderTraversal(n.left)
            if n.right: self.PreOrderTraversal(n.right)
        
    def InOrderTraversal(self, n=None):
        '''
        Prints nodes in the order: left child, current, right child.
        Args:
            n: Root node of the tree (optional)
        '''
        
        #implement using recursion
        if n==None:
            n=self.root
     
        if n.left==None and n.right ==None:
            print(n.val, end= " ")
            return
        else:
            if n.left: self.InOrderTraversal(n.left)
            print (n.val, end=" ")
            if n.right: self.InOrderTraversal(n.right)
                    
        
def main():
    mBT=BTree(5)
    mBT.add(3)
    mBT.add(4)
    mBT.add(2)
    mBT.add(6)
    mBT.add(8)
    mBT.add(1)
    mBT.add(0)
    mBT.add(7)
    mBT.printTree()

    print("Pre Order Traversal...\n")
    mBT.PreOrderTraversal()

    print("\n\nPost Order Traversal...\n")
    mBT.PostOrderTraversal()

    print("\n\nIn Order Traversal...\n")
    mBT.InOrderTraversal()

if __name__=="__main__":
    main()


#Output 

# Printing Tree...
#        5  
#       3  6  
#      2  4  8  
#     1  7  
#    0  
  
# Pre Order Traversal...

# 5 3 2 1 0 4 6 8 7 

# Post Order Traversal...

# 0 1 2 4 3 7 8 6 5 

# In Order Traversal...

# 0 1 2 3 4 5 6 7 8 