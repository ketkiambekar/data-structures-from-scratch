class node:
    def __init__(self, dataval):
        self.val = dataval
        self.next = None
        self.prev = None

class dLinkedList:
    def __init__(self, val):
        n= node(val)
        self.head = n
        self.tail = n
        #create a node   

    def insert(self, val):
        '''
        Adds a node to the end of the Linkedlist. 

        Args:
            val : Value of the node to be inserted
        Returns: 
            Nothing
        '''
        n=node(val)
        n.prev =self.tail
        self.tail.next =n
        self.tail = n
        
        
        
    

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
        print("Printing LinkedList...")
        print("Head node: ",self.head.val)
        print("Tail node: ",self.tail.val)
        ll=self.head
        while True:
            print(ll.val)
            if ll.next==None:
                break
            ll = ll.next
    
    def print_list_reverse(self):
        '''
        Prints all the nodes in the Linkedlist.

        Args:
           None
        '''
        print("Printing LinkedList Reversed...")
        print("Head node: ",self.head.val)
        print("Tail node: ",self.tail.val)
        ll=self.tail
        while True:
            print(ll.val)
            if ll.prev==None:
                break
            ll = ll.prev
        

def main():
    
    #create linked list, pass the value of first node in the args
    l1 = dLinkedList("A")
    l1.print_list()
    l1.print_list_reverse()

    l1.insert("B")
    l1.print_list()
    l1.print_list_reverse()

    l1.insert("C")
    l1.insert("D")
    l1.insert("K")
    l1.insert("N")

    l1.print_list()
    l1.print_list_reverse()

    print("Popped:" ,l1.pop("D"))
    l1.print_list()

    print("Popped:" ,l1.pop("N"))
    l1.print_list()

    print("Popped:", l1.pop("A"))
    l1.print_list()
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



