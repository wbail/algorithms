class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def printTheList(self):
        
        curr = self.head
        
        while curr:
            print(curr.value)
            curr = curr.next
        
    def insertEnd(self, node):
    
        if self.head == None:
            self.head = node
        else:
            curr = self.head
        
            while curr.next:
                curr = curr.next
                
            curr.next = node
    
    def insertBeginng(self, node):
        
        if self.head == None:
            self.head = node
        else:
            # To be inserted: 1
            # 7 -> 77 -> 90
            # 1 -> 7 -> 77 -> 90
            oldHead = self.head
            self.head = node
            node.next = oldHead

    def insertAfter(self, node, afterNode):
        # Value to be inserted: 28 after 14
        # 7 -> 14 -> 21
        # 7 -> 14 -> 28 -> 21
        
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            
            while curr:
                if curr.value == afterNode.value:
                    nextNode = curr.next
                    curr.next = node
                    node.next = nextNode
                    
                curr = curr.next
    
    def delete(self, node):
        if self.head == None:
            print('List is empty.')
        else:
            curr = self.head
            
            while curr:
                
                # 7 -> 14 -> 21
                # Delete 14
                # 7 -> 21
                
                if curr.next:
                    nextNode = curr.next
                    if nextNode.value == node.value:
                        curr.next = nextNode.next
               
                curr = curr.next
                
    def reverse(self):
        # TODO: Reverse the list

node = Node()
node.value = 7

node1 = Node()
node1.value = 14

node2 = Node()
node2.value = 21

node3 = Node()
node3.value = 28

node4 = Node()
node4.value = 35

linkedList = LinkedList()

linkedList.insertEnd(node)
linkedList.insertEnd(node1)

print('Inserting the values', node.value, ',' , node1.value, 'in the end.')

print('======= Printing the List =======')
linkedList.printTheList()

linkedList.insertBeginng(node2)

print('Inserting the value', node2.value, 'in the beginning.')

print('======= Printing the List =======')
linkedList.printTheList()

print('Inserting the value', node3.value, 'after the value', node1.value)

linkedList.insertAfter(node3, node1)

print('======= Printing the List =======')
linkedList.printTheList()

print('Inserting the value', node4.value, 'after the value', node1.value)

linkedList.insertAfter(node4, node1)

print('======= Printing the List =======')
linkedList.printTheList()

print('Deleting the value', node1.value)

linkedList.delete(node1)

print('======= Printing the List =======')
linkedList.printTheList()

print('Reverse the list')
linkedList.reverse()