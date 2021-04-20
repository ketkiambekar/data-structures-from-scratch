class node:
    def __init__(self, dataval):
        self.val = dataval
        self.next = None

class sLinkedList:
    def __init__(self, val):
        self.head = node(val)
        #create a nodeaqc   

    def insert(self, val):
        '''
        Adds a node to the Linkedlist. 

        Args:
            val : Value of the node to be inserted
        Returns: 
            Nothing
        '''
        ll =self.head
        while ll.next!=None:
            ll = ll.next
        ll.next = node(val)

    def pop(self, val):
        '''
        Deletes a node from the Linkedlist and returns the deleted item.

        Args:
            val : Value of the node to be deleted. (If there are two nodes of the same value, the first occurrence will be deleted.)
        
        Returns:
            The value of deleted node. 
        '''
        ll = self.head

        #We have two cases:
        # Case 1: Deleting the head node
        if ll.val == val:
            self.head = ll.next
            return ll.val

        #Case 2: Deleting a non-head node.
        while True:
            if ll.next.val == val:
                temp = ll.next.val
                ll.next = ll.next.next
                return temp
            if ll.next == None:
                print("Node not found in the Linkedlist")
                return
            ll=ll.next


    def print_list(self):
        '''
        Prints all the nodes in the Linkedlist.

        Args:
           None
        '''
        ll=self.head
        while True:
            print(ll.val)
            if ll.next==None:
                break
            ll = ll.next
        

def main():
    
    #create linked list, pass the value of first node in the args
    l1 = sLinkedList("A")
    l1.insert("B")
    l1.insert("C")
    l1.insert("D")
    l1.insert("K")
    l1.insert("N")

    l1.print_list()

    print("Popped:" ,l1.pop("D"))
    l1.print_list()

    print("Popped:" ,l1.pop("N"))
    l1.print_list()

    print("Popped:", l1.pop("A"))
    l1.print_list()

if __name__=="__main__":
    main()
    
   
########### OUTPUT ###########
    # A
    # B
    # C
    # D
    # K
    # N
    # Popped: D
    # A
    # B
    # C
    # K
    # N
    # Popped: N
    # A
    # B
    # C
    # K
    # Popped: A
    # B
    # C
    # K
####################################



