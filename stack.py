class Stack(list): #Inherit the built-in class List
    
    def push(self,val):
        self.insert(0,val)
        print("Pushed: ", val)

    def popVal(self):
        if len(self)==0:
            print("Stack is empty. Nothing to pop.")
        else:
            popped = self.pop(0)
            print("Popped: ", popped)
            

    def printStack(self):
        print("Printing stack...")
        print(self)
        
    
def main():
    myStack = Stack()

    myStack.popVal()
    myStack.push(4)
    myStack.push("Valerie")
    myStack.push(["as","you","know"])
    myStack.printStack()
    myStack.popVal()
    myStack.push(2.4)
    myStack.printStack()
    myStack.popVal()
    myStack.popVal()

    myStack.printStack()



if __name__=="__main__":
    main()
    


########## OUTPUT ########

# Stack is empty. Nothing to pop.

# Pushed:  4
# Pushed:  Valerie
# Pushed:  ['as', 'you', 'know']

# Printing stack...
# [['as', 'you', 'know'], 'Valerie', 4]

# Popped:  ['as', 'you', 'know']

# Pushed:  2.4

# Printing stack...
# [2.4, 'Valerie', 4]

# Popped:  2.4
# Popped:  Valerie

# Printing stack...
# [4]

##############################
