class node:
    def __init__(self, dataval):
        self.data = dataval
        self.next = None

class sLinkedList:
    def __init__(self, val):
        self.head = node(val)
        #create a nodeaqc   

    def insert(self, val):
        ll =self.head
        while ll.next!=None:
            ll = ll.next
        ll.next = node(val)

    def delete(self, val):
        pass

    def print_list(self):
        ll=self.head
        while True:
            print(ll.val)
            if ll.next==None:
                break
            ll = ll.next
        



def main():
    
    #create linked list, pass the value of first node in the args
    l1 = sLinkedList("Apple")



