class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None
        self.size=0

    def insert_at_start(self,data):
        self.size=self.size+1
        NewNode=Node(data)
        
        if not self.head:
            self.head=NewNode
        else:
            NewNode.next=self.head
            self.head=NewNode
    # O(1)
    def size(self):
        return self.size
    # O(n)
    def size2(self):
        size=0
        ActualNode=self.head

        while ActualNode in not None:
            size+=1
            ActualNode=ActualNode.next

        return size

    def insert_at_end(self, data):
        self.size=self.size+1
        NewNode=Node(data)

        ActualNode=self.head

        while ActualNode.next is not None:
            ActualNode=ActualNode.next

        ActualNode.next=NewNode

    def remove(self, data):
        if self.head is None:
            return

        self.size=self.size-1
        CurrentNode=self.head
        previousNode= None

        while currentNode.data != data:
            previousNode=currentNode
            currentNode=currentNode.next

        if previousNode is None:
            self.head=currentNode.nextNode
        else:
            previousNode.nextNode=currentNode.nextNode

    
        

        
