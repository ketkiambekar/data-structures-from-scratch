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
        #Queue that contains all nodes
        q1 =[self.root, None]
        levels =0


        #Populate the queue
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

if __name__=="__main__":
    main()


#Output 
#        5  
#       3  6  
#      2  4  8  
#     1  7  
#    0  
  