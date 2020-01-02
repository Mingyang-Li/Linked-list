class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head):
        self.head = None
    
    def insertHead(self, newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode = newNode

    def printList(self):
        currentNode = self.head
        while True:
            if currentNode.next is None:
                break
            print(currentNode)
            currentNode = currentNode.next

firstGuy = Node("Bob")
fancyList = linkedList(firstGuy)
fancyList.insert(firstGuy)

secondGuy = Node("Caleb")
fancyList = linkedList(secondGuy)
fancyList.insert(secondGuy)

thirdGuy = Node("Dave")
fancyList = linkedList(thirdGuy)
fancyList.insert(thirdGuy)

fourthGuy = Node("NEW GUY")
fancyList = linkedList(fourthGuy)
fancyList.insertHead(fourthGuy)

fancyList.printList()

              
